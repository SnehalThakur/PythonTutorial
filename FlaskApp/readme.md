**Flask**

Flask is a small and lightweight Python web framework that provides useful tools and features that make creating web applications in Python easier.

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
if __name__ == "__main__":
    app.run()
```
