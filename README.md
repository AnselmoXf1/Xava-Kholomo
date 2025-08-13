# xava-kholomo Flask Application

This is a Flask web application for showcasing and selling online courses and digital products. The application includes features such as product listings, detailed product views, a contact form, and a checkout process.

## Project Structure

```
xava-kholomo
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── README.md             # Project documentation
├── templates             # HTML templates for rendering pages
│   ├── index.html
│   ├── product.html
│   ├── about.html
│   ├── contact.html
│   ├── checkout.html
│   └── confirmation.html
└── static                # Directory for static files (CSS, JS, images)
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd xava-kholomo
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application locally:**
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Deployment on Vercel

To deploy this application on Vercel, ensure you have the `vercel.json` file configured correctly. You can deploy by running:

```bash
vercel
```

Follow the prompts to complete the deployment process.

## Usage

- Navigate to the homepage to view the list of products.
- Click on a product to view its details.
- Use the contact form to send messages.
- Proceed to checkout to purchase a product.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.