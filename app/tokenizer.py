from typing import List, Union
from pathlib import Path
import base64


class Tokenizer:
    def __init__(self, model_path: Union[str, Path]):
        """Initialize the tokenizer with the vocabulary file."""
        self.token_to_id = {}
        self.id_to_token = {}

        with open(model_path, "r") as f:
            for line in f:
                token_b64, token_id = line.strip().split()
                token_id = int(token_id)
                token = base64.b64decode(token_b64).decode("utf-8", errors="replace")
                self.token_to_id[token] = token_id
                self.id_to_token[token_id] = token

    def encode(self, text: Union[str, List[str]]) -> Union[List[int], List[List[int]]]:
        """Encode text into token ids."""
        if isinstance(text, str):
            return [self.token_to_id[c] for c in text if c in self.token_to_id]
        return [self.encode(t) for t in text]

    def decode(
        self, token_ids: Union[List[int], List[List[int]]]
    ) -> Union[str, List[str]]:
        """Decode token ids back into text."""
        if not token_ids:  # Handle empty list case
            return ""
        if isinstance(token_ids[0], int):
            return "".join(
                self.id_to_token[id] for id in token_ids if id in self.id_to_token
            )
        return [self.decode(ids) for ids in token_ids]
