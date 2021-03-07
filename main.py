from website import create_app

app = create_app()

#only if you run this file directly will the website start (per the below code)
if __name__ == '__main__':
    app.run(debug=True)