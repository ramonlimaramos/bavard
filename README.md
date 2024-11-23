# Bavard

_This project is under development not ready_

This project is a simple and customizable Text-to-Speech (TTS) application that converts input text into audio using a pre-trained PyTorch model (`model.pth`). The intuitive web interface allows you to upload your TTS model, input text, and generate speech.

<img src="https://raw.githubusercontent.com/ramonlimaramos/bavard/main/.github/bavard.png" />

---

## Key Features
- **Model Upload:** Load your pre-trained TTS model in `.pth` format.
- **Text Input:** Enter any text you want to convert into speech.
- **Audio Generation:** Generate and download the speech audio file.

---

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Pyramid
- PyTorch
- TorchAudio

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-to-speech-app.git
   cd bavard
   ```

2. Install the dependencies:
   ```bash
   poetry install
   ```

3. Run the application:
   ```bash
   poetry serve
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:6543
   ```

---

## How to Use
1. **Upload Model:** Click "Choose File" to upload your `model.pth` file.
2. **Enter Text:** Type the desired text in the input box.
3. **Generate Speech:** Click the "Generate Speech" button to convert the text into an audio file.
4. **Playback or Download:** Listen to the generated audio or download it.

---

## Folder Structure
```
.
├── services                 # Pytorch services comsuption
├── static/                  # Static files (CSS, JS)
├── templates/               # HTML templates
├── controllers.py           # MVC Controllers
├── routes.py                # Pyramid routes
├── scripts.py               # Poetry tasks scripts
└── views.py                 # MVC Views
```

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you'd like to add new features or improvements.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For any questions or suggestions, feel free to reach out:
- Email: [ramonlimaramos@gmail.com](mailto:ramonlimaramos@gmail.com)
- GitHub: [@ramonlimaramos](https://github.com/ramonlimaramos)