import torch
import torchaudio
import tempfile
import os

class TTSService:
    def __init__(self):
        self.model = None
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    def load_model(self, model_file):
        self.model = torch.load(model_file, map_location=self.device)
        self.model.eval()
    
    def generate_speech(self, text):
        if self.model is None:
            raise ValueError("Model not loaded")
            
        with torch.no_grad():
            # This is a placeholder for the actual model inference
            # You'll need to implement the specific model logic here
            waveform = self.model(text)
            
            # Save to temporary file
            temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
            torchaudio.save(temp_file.name, waveform, 22050)
            
            return temp_file.name 