# NutriSnap

A Streamlit-powered nutrition analysis tool that uses Google's Gemini 1.5 Flash LLM model to provide personalized health insights from nutrition label images, with a specific focus on women's nutritional needs.

## Overview

NutriSnap analyzes nutrition labels through image capture or upload and provides clear, actionable feedback about the nutritional value of food items. Powered by Google's Gemini 1.5 Flash LLM model, it evaluates key nutrients particularly important for women's health, including iron and calcium, while offering practical alternatives for less healthy options.

View the running app here: https://nutri-snap.streamlit.app

## Features

- 📸 Image capture or upload of nutrition labels
- 🤖 Advanced analysis using Gemini 1.5 Flash LLM
- 👩 Women's health-focused insights
- 📊 Visual health rating system
- 🔄 Healthy alternative suggestions
- 📝 Educational nutrition information

## Requirements

- Python 3.8+
- Streamlit
- Google Gemini 1.5 Flash API access (requires obtaining an API key [here](https://aistudio.google.com/app/apikey))
- Additional dependencies listed in `requirements.txt`

## Installation

```bash
git clone https://github.com/sdbenezra/nutrisnap
cd nutrisnap
pip install -r requirements.txt
echo export GOOGLE_API_KEY=<your API key> >> ~/.zshrc
source ~/.zshrc
```

## Running the App

Navigate to the directory containing the app.py file.
Start the Streamlit app with:
```bash
streamlit run app.py
```

## Usage

1. Launch the app using the command above
2. Choose your preferred input method:
   - Take a picture using your device's camera
   - Upload an existing image file
3. Review the detailed analysis of the nutritional content
4. Check the health rating and any suggested alternatives

## Health Rating Scale

NutriSnap uses a three-point rating scale to evaluate foods:
- 🟢 **Healthy**: Nutritionally dense, beneficial for overall health
- 🟡 **Moderate**: Some concerns but generally acceptable
- 🔴 **Low**: Consider healthier alternatives

## Disclaimer

This app provides educational information only, not medical advice. Nutritional needs vary by individual. Always consult your healthcare provider before making dietary changes. Do not rely on this app in place of professional medical guidance.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or suggestions, please open an issue in the GitHub repository.