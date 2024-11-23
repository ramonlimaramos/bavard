async function uploadModel() {
    const fileInput = document.getElementById('model-file');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select a model file');
        return;
    }
    
    const formData = new FormData();
    formData.append('model', file);
    
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            alert('Model uploaded successfully');
        } else {
            alert('Failed to upload model');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error uploading model');
    }
}

async function generateSpeech() {
    const text = document.getElementById('input-text').value;
    
    if (!text) {
        alert('Please enter some text');
        return;
    }
    
    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text })
        });
        
        if (response.ok) {
            const blob = await response.blob();
            const audioUrl = URL.createObjectURL(blob);
            
            const audioPlayer = document.getElementById('audio-player');
            const downloadLink = document.getElementById('download-link');
            const audioOutput = document.getElementById('audio-output');
            
            audioPlayer.src = audioUrl;
            downloadLink.href = audioUrl;
            downloadLink.download = 'generated_speech.wav';
            audioOutput.style.display = 'block';
        } else {
            alert('Failed to generate speech');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error generating speech');
    }
} 