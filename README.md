Sentiment Analyzer using RoBERTa + Flask + Tailwind
----------------------------------------------------

This project is a full-stack web application that performs sentiment analysis using a fine-tuned RoBERTa transformer model. The app provides a simple interface to enter any text, and it returns whether the sentiment is positive or negative, along with a confidence score.

----------------------------------------------------
KEY FEATURES:
----------------------------------------------------
- Simple and responsive UI using Tailwind CSS
- Flask backend for handling inference requests
- Hugging Face Transformers pipeline using RoBERTa
- Displays confidence score and sentiment with visual styling

----------------------------------------------------
HOW IT WORKS:
----------------------------------------------------
1. The user enters text on the website.
2. A POST request is sent to the Flask backend (`/predict`).
3. The backend loads the fine-tuned RoBERTa model and predicts:
   - Label: positive / negative
   - Score: model confidence
4. The result is shown on the frontend with color-coded styling.

----------------------------------------------------
MODEL SETUP (IMPORTANT):
----------------------------------------------------
To run this app, you must download the pre-trained sentiment model and place it in the project root directory as `sentiment_model_roberta`.

Download the model from:
https://drive.google.com/drive/folders/1EEQKGYYeIsvddoQLptXCae0qXaVt9c61?usp=drive_link

After downloading, place the entire folder in the same directory as `app.py`.

----------------------------------------------------
NOTEBOOK SETUP (OPTIONAL):
----------------------------------------------------
If you wish to explore or fine-tune the model using the included Jupyter notebook (`sentiment_user.ipynb`), you will also need the dataset.

Download the dataset from:
https://drive.google.com/file/d/1d56ZnY8NJ9mWEL4SY3I-oQY9mKIW-FGK/view?usp=sharing

Once downloaded, place the dataset file in the same folder as `sentiment_user.ipynb`.

----------------------------------------------------
FILE STRUCTURE:
----------------------------------------------------
app.py                    - Flask backend app
templates/index.html      - Frontend with Tailwind CSS
sentiment_model_roberta/  - Pretrained and fine-tuned RoBERTa model (downloaded)
sentiment_user.ipynb      - Jupyter notebook used to test/load model
README.txt                - This file
myenv/                    - Virtual environment (not committed)

----------------------------------------------------
HOW TO RUN LOCALLY:
----------------------------------------------------
1. Clone the repository:
   git clone https://github.com/<your-username>/sentiment-analyzer.git
   cd sentiment-analyzer

2. Create and activate a virtual environment:
   python3 -m venv myenv
   source myenv/bin/activate

3. Install the required dependencies:
   pip install -r requirements.txt

4. Ensure that the `sentiment_model_roberta/` folder is in the project root.

5. Run the Flask app:
   python3 app.py

6. Open your browser at:
   http://localhost:5000

----------------------------------------------------
SAMPLE OUTPUT:
----------------------------------------------------
Input:    "I really love this product!"
Output:   Sentiment: Positive
          Confidence: 96.78%

Input:    "IThe film we watched was horrible"
Output:   Sentiment: Negative
          Confidence: 99.00%

----------------------------------------------------
MODEL INFO:
----------------------------------------------------
- Model used: RoBERTa (fine-tuned on sentiment classification)
- Framework: Hugging Face Transformers
- Stored locally inside `sentiment_model_roberta/`
- Output labels: LABEL_0 = Negative, LABEL_1 = Positive

----------------------------------------------------
TECH STACK:
----------------------------------------------------
Frontend:  HTML, Tailwind CSS, JavaScript
Backend:   Python, Flask
ML Model:  Hugging Face RoBERTa

