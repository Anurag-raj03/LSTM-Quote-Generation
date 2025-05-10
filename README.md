

---

# ✨🧠 LSTM-Based Quote Generator 🚀📜

---

## 🌟 Project Overview

Hello Innovators! 👋
I'm thrilled to present my latest deep learning project — **LSTM-Based Quote Generator**! 🎉

This project demonstrates the potential of **LSTM (Long Short-Term Memory)** networks for **text generation**, creating inspiring quotes based on a given **seed text**. 📝✨

🔗 **LinkedIn Demo Post**: [Check the Demo Here 🚀](https://www.linkedin.com/posts/anurag-raj-770b6524a_machinelearning-nlp-deeplearning-activity-7223656733250842624-nHkK?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD3AcAQBbDZknKOXA3z1RQH_Xu2ftPQQWKI)

🔗 **Kaggle Notebook**: [View Full Project on Kaggle 📚](https://www.kaggle.com/code/anuragraj03/quote-generator-lstm)

🔗 **GitHub Repository**: [Explore Codebase on GitHub 💻](https://github.com/Anurag-raj03/LSTM-Quote-Generation)

---

## 📸 Quick Features Overview

| Feature                   | Description                                                |
| :------------------------ | :--------------------------------------------------------- |
| 📝 **Seed Text Input**    | Input a starting phrase to inspire your quote generation   |
| 🔢 **Word Count Slider**  | Choose how many words you want in your generated quote     |
| ✨ **Instant Generation**  | Click a button and instantly get a unique, coherent quote  |
| 🚀 **FastAPI Deployment** | Model integrated into a lightweight API for fast responses |
| 🎨 **Advanced UI/UX**     | Clean, gradient-styled interface with interactive elements |

---

## 🛠️ Tech Stack

| 📚 Technology               | 🚀 Purpose                               |
| :-------------------------- | :--------------------------------------- |
| **Python**                  | Core programming language                |
| **TensorFlow / Keras**      | Deep learning and LSTM model development |
| **FastAPI**                 | API deployment for the model             |
| **Jupyter Notebook**        | Experimentation and prototyping          |
| **HTML, CSS (Gradient UI)** | Front-end for better user interaction    |

---

## 🏗️ Project Workflow

### 📥 1. Data Preparation

* 📂 **Custom Dataset**: Generated my own **quotes dataset**.
* 🧹 **Text Cleaning**:

  * Lowercased all text.
  * Removed special characters and punctuations.
* ✂️ **Tokenization**:

  * Used **Keras Tokenizer** to convert text into sequences.
  * Created **n-gram sequences** for next-word prediction training.

### 🧠 2. Model Building

* 🏗️ Built an **LSTM**-based sequential model.
* Layers:

  * **Embedding Layer** to learn word representations.
  * **Two LSTM Layers** to capture context and sequence information.
  * **Dense Layer** with softmax activation for word prediction.

### 🏋️ 3. Model Training

* Categorical cross-entropy loss.
* Adam optimizer with early stopping.
* Achieved **good convergence and accuracy** for quote generation.

### 🛠️ 4. FastAPI Deployment

* Created a lightweight **FastAPI** backend to serve the model.
* Exposed an endpoint where:

  * **Input**: Seed text and number of words.
  * **Output**: Dynamically generated quote.

### 🎨 5. Front-End UI/UX

* Clean web design:

  * Gradient background 🎨
  * Input box for seed text ✍️
  * Word count slider 🎛️
  * "Generate Quote" button 🖱️

### 📈 6. Testing & Evaluation

* Validated model with multiple inputs.
* Observed **contextual and coherent** quote generation.

---

## 📋 How to Run Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Anurag-raj03/LSTM-Quote-Generation.git
   cd LSTM-Quote-Generation
   ```

2. **Install Required Libraries**
   *(Make sure you are using Python 3.7+)*

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI App**

   ```bash
   uvicorn app:app --reload
   ```

4. **Access the App**

   * Open your browser and visit:
     `http://127.0.0.1:8000`
   * Or try the API docs at:
     `http://127.0.0.1:8000/docs`

---

## 🖼️ Project Snapshot

| 📸                                  | ✨                                      |
| :---------------------------------- | :------------------------------------- |
| Beautiful gradient UI 🎨            | Instantly generate inspiring quotes 💬 |
| Easy-to-use text box and slider 🛠️ | Real-time quote generation 🚀          |

---

## 🎯 Key Results

* ✅ Successfully generated coherent quotes.
* ✅ Fast API response time using **FastAPI**.
* ✅ User-friendly interface for seamless interaction.
* ✅ Fully **open-source** dataset and code for community use.

---

## 🚀 Future Work

* Fine-tune the model using **transfer learning** on bigger corpora (e.g., famous authors’ quotes).
* Improve the grammar by applying **language models** (e.g., GPT fine-tuning).
* Build a mobile application for **on-the-go quote generation** 📱✨.
* Add **multi-language quote generation** support 🌍.

---

## 🤝 Connect With Me

I'm super excited to share this project with the community! 🌟
Feel free to explore the code, dataset, and notebook.
Your feedback and suggestions are most welcome! 🙏🏻

* 🔗 [LinkedIn](https://www.linkedin.com/in/anurag-raj-770b6524a/)
* 🐙 [GitHub](https://github.com/Anurag-raj03)
* 📊 [Kaggle](https://www.kaggle.com/anuragraj03)

---

## 📌 Hashtags

\#MachineLearning #NLP #DeepLearning #QuoteGenerator #AI #FastAPI #Kaggle #Project #LSTM #TextGeneration #ArtificialIntelligence #Python #Innovation

---

