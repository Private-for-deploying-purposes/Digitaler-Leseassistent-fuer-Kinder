from sklearn.metrics import f1_score
import numpy as np
from transformers import DistilBertTokenizerFast, DistilBertForQuestionAnswering, Trainer, TrainingArguments
from datasets import load_dataset
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

def compute_f1_and_em(predictions, references):
    """
    Computes the F1 score and Exact Match (EM) metrics.
    
    Args:
        predictions (list): List of predicted answers.
        references (list): List of ground truth answers.
        
    Returns:
        dict: Dictionary containing F1 score and EM score.
    """
    f1_scores = []
    em_scores = []
    
    for pred, ref in zip(predictions, references):
        # Normalize text (lowercase and remove extra spaces)
        pred = pred.lower().strip()
        ref = ref.lower().strip()
        
        # Exact Match
        em_scores.append(pred == ref)
        
        # F1 Score
        pred_tokens = pred.split()
        ref_tokens = ref.split()
        
        common = set(pred_tokens) & set(ref_tokens)
        num_common = len(common)
        
        if num_common == 0:
            f1_scores.append(0)
        else:
            precision = num_common / len(pred_tokens)
            recall = num_common / len(ref_tokens)
            f1_scores.append(2 * (precision * recall) / (precision + recall))
    
    avg_f1 = np.mean(f1_scores)
    avg_em = np.mean(em_scores)
    
    return {"f1": avg_f1, "exact_match": avg_em}

def evaluate_model(model, tokenizer, dataset):
    """
    Evaluates the model on the validation dataset using F1 score and EM.
    
    Args:
        model: The fine-tuned model.
        tokenizer: Tokenizer instance.
        dataset: Validation dataset to evaluate.
        
    Returns:
        dict: Dictionary containing F1 score and EM score.
    """
    predictions = []
    references = []
    
    for example in dataset:
        question = example["question"]
        context = example["context"]
        reference_answer = example["answers"]["text"][0]  # First ground truth answer
        
        # Get the model's prediction
        pred_answer = answer_question(question, context, model, tokenizer)
        
        predictions.append(pred_answer)
        references.append(reference_answer)
    
    # Compute metrics
    metrics = compute_f1_and_em(predictions, references)
    return metrics


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
train_dataset, validation_dataset = load_data()

# Example usage
if __name__ == "__main__":
    # Define paths
    #model_path = "./distilbert-qa"  # Path where the model is saved
    model_path = "mxhmxt/distilbert-qa-digital-reading-assistant-for-children" 
    # Load model and tokenizer
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
    model = DistilBertForQuestionAnswering.from_pretrained(model_path)
    # Evaluate the fine-tuned model on the validation dataset
    metrics = evaluate_model(model, tokenizer, validation_dataset)
    print(f"Evaluation Results:\nF1 Score: {metrics['f1']:.4f}\nExact Match: {metrics['exact_match']:.4f}")



# Evaluation Results:
# F1 Score: 0.6794
# Exact Match: 0.5019
