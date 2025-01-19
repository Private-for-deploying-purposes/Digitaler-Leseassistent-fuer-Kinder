# Install the required libraries
# Run the following in your terminal or Colab notebook if not installed:
# !pip install transformers datasets torch

from datasets import load_dataset
from transformers import DistilBertTokenizerFast, DistilBertForQuestionAnswering, Trainer, TrainingArguments
import torch

# Step 1: Load Dataset (SQuAD in this example)
def load_data():
    """
    Loads the SQuAD dataset for question answering tasks.
    Returns the training and validation datasets.
    """
    dataset = load_dataset("squad")
    train_dataset = dataset["train"]
    validation_dataset = dataset["validation"]
    return train_dataset, validation_dataset

# data_train, data_val = load_data()
# print(data_train)


# Step 2: Tokenize the Dataset
def tokenize_data(dataset, tokenizer):
    """
    Tokenizes the dataset and computes the start and end positions of answers.
    Args:
        dataset: The dataset to preprocess.
        tokenizer: The tokenizer instance.
    Returns:
        Tokenized dataset with start_positions and end_positions added.
    """
    def preprocess(batch):
        """
        Preprocesses a batch of examples to tokenize and compute start and end positions.
        Args:
            batch: A batch of examples from the dataset.
        Returns:
            Tokenized batch with start_positions and end_positions added.
        """
        tokenized = tokenizer(
            batch["question"],
            batch["context"],
            truncation=True,
            padding="max_length",
            max_length=384,
            return_offsets_mapping=True
        )

        start_positions = []
        end_positions = []

        for i in range(len(batch["context"])):
            # Extract the start and end character positions of the first answer
            start_char = batch["answers"][i]["answer_start"][0]
            end_char = start_char + len(batch["answers"][i]["text"][0])

            # Get the offset mapping for this example
            offsets = tokenized["offset_mapping"][i]

            # Find the token indices corresponding to the start and end character positions
            start_idx = 0
            end_idx = 0
            for j, (offset_start, offset_end) in enumerate(offsets):
                if offset_start <= start_char < offset_end:
                    start_idx = j
                if offset_start < end_char <= offset_end:
                    end_idx = j

            start_positions.append(start_idx)
            end_positions.append(end_idx)

        tokenized["start_positions"] = start_positions
        tokenized["end_positions"] = end_positions

        # Remove offset mapping as it is not needed for training
        tokenized.pop("offset_mapping", None)

        return tokenized



    return dataset.map(preprocess, batched=True)


# Step 3: Prepare Dataset for PyTorch
def prepare_features(tokenized_dataset):
    """
    Prepares features for PyTorch training.
    """
    tokenized_dataset.set_format(
        type='torch',
        columns=['input_ids', 'attention_mask', 'start_positions', 'end_positions']
    )

# Step 4: Fine-Tune DistilBERT
def train_model(train_dataset, validation_dataset, tokenizer):
    """
    Fine-tunes DistilBERT on the provided datasets.
    Args:
        train_dataset: The training dataset.
        validation_dataset: The validation dataset.
        tokenizer: The tokenizer instance.
    """
    model = DistilBertForQuestionAnswering.from_pretrained("distilbert-base-uncased")
    
    # Define Training Arguments
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="steps",
        eval_steps=500,
        save_steps=500,
        logging_steps=100,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=2,
        save_total_limit=2,
        learning_rate=3e-5,
        weight_decay=0.01,
        logging_dir='./logs'
    )

    #model.gradient_checkpointing_enable()
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=validation_dataset,
        tokenizer=tokenizer
    )

    # Train the model
    trainer.train()
    trainer.save_model("./distilbert-qa")

    return model

# Step 5: Inference Function
import torch

def answer_question(question, context, model, tokenizer):
    """
    Answers a question using the fine-tuned model.
    Args:
        question: The question to answer.
        context: The context containing the answer.
        model: The fine-tuned model.
        tokenizer: The tokenizer instance.
    Returns:
        Answer string.
    """
    # Check device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Tokenize inputs and move them to the same device as the model
    inputs = tokenizer(
        question,
        context,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=384
    ).to(device)  # Move inputs to the correct device

    with torch.no_grad():
        outputs = model(**inputs)
        start_logits = outputs.start_logits
        end_logits = outputs.end_logits

    # Get the most probable start and end positions
    start_idx = torch.argmax(start_logits)
    end_idx = torch.argmax(end_logits)

    # Decode the answer
    answer = tokenizer.decode(inputs["input_ids"][0][start_idx:end_idx + 1])
    return answer


# Execute the workflow
if __name__ == "__main__":
    # Load datasets
    train_dataset, validation_dataset = load_data()

    # Initialize the tokenizer
    tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

    # Tokenize the datasets
    tokenized_train = tokenize_data(train_dataset, tokenizer)
    tokenized_val = tokenize_data(validation_dataset, tokenizer)

    # Prepare the datasets for PyTorch
    prepare_features(tokenized_train)
    prepare_features(tokenized_val)
    
    # Fine-tune the model
    model = train_model(tokenized_train, tokenized_val, tokenizer)

    # Test the model with an example
    question = "What is the capital of France?"
    context = "France's capital is Paris, which is a major European city."
    answer = answer_question(question, context, model, tokenizer)
    print(f"Question: {question}")
    print(f"Answer: {answer}")
