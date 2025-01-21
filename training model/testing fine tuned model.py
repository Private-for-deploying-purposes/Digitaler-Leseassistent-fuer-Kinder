from transformers import DistilBertTokenizerFast, DistilBertForQuestionAnswering
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

# Define paths
model_path = "distilbert-qa"  # Path where the model is saved

# Load model and tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
model = DistilBertForQuestionAnswering.from_pretrained(model_path)

# Example test
question = "what is bennis uncle?"
context = "Benni is supposed to give a presentation in his class about the professions his family practices. He says his uncle is a firefighter. Benni has often been allowed to sit in the fire truck. Once, his uncle was called to an emergency and had to extinguish a fire in a family house. Benni is not allowed to ride along on such calls. But he can on less dangerous tasks. An injured cat was stuck in a tree and couldn't get down. Benni was allowed to help. The boy tried to lure the cat. He succeeded and took the cat in his arms. He slowly climbed down the ladder and was happy to have been part of a fire emergency. Benni's class was thrilled when he told the story and stood proudly in front of them."

answer = answer_question(question, context, model, tokenizer)
print(f"Question: {question}")
print(f"Answer: {answer}")

