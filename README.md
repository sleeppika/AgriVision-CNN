# AgriVision-CNN — DKA3223 Practice Project

> This folder is a practice/reference project. Run the files yourself and use
> your own screenshots, Git history, GitHub repository, and report for any
> assessed work.

## Project structure

```text
AgriVision-CNN/
├── data/
├── dataset_handler.py
├── cnn_model.py
├── train.py
├── requirements.txt
├── README.md
└── REPORT_TEMPLATE.md
```

## 1. Install libraries

```bash
pip install -r requirements.txt
```

## 2. Test dataset visualisation

```bash
python dataset_handler.py
```

Expected result: a Matplotlib window showing 3 CIFAR-10 sample images and labels.

## 3. Test CNN training

```bash
python train.py
```

The training script demonstrates:

- Learning Rate = 0.001
- Epochs = 3
- Batch Size = 32
- Forward propagation
- Loss calculation
- Backward propagation
- Optimizer update
- Python `for` loops

## 4. Git workflow to practise

Use your own GitHub account and repository. Do not fabricate screenshots or
commit history.

Example command sequence:

```bash
git init
git add .
git commit -m "Initial AgriVision CNN project"

git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main

git checkout -b feature-hyperparameter
git add dataset_handler.py cnn_model.py train.py
git commit -m "Add CNN training and hyperparameters"
git push -u origin feature-hyperparameter
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your own repository.

## 5. What to screenshot

Take your own screenshots after successfully running the project:

1. Matplotlib showing 3 sample images + labels.
2. Terminal/IDE showing the 3 training epochs and loss values.
3. GitHub showing the repository and `feature-hyperparameter` branch.
4. Commit history showing a relevant commit message.
5. Google Classroom upload page, if your lecturer requires it.

Do not create fake output values or fake GitHub screenshots.
