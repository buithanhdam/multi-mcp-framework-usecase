# Multi-MCP Framework Usecase

This project demonstrates the use of the **MCP framework** with various tools and frameworks such as **Google ADK, LlamaIndex, LangChain**, and an **MCP adapter**.  
It includes a **client-server setup** for testing and interacting with the MCP framework.

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- Python **3.10** or higher  
- Git  
- A terminal or command prompt  

---

## ⚙️ Setup Instructions

Follow these steps to clone the repository, set up the environment, and run the project:

### 1. Clone the Repository
```bash
git clone https://github.com/buithanhdam/multi-mcp-framework-usecase.git
cd multi-mcp-framework-usecase
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
```

On **Windows**:

```bash
venv\Scripts\activate
```

On **macOS/Linux**:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run MCP Inspect

To inspect the MCP setup, run:

```bash
# Go to the server folder
cd src/base_mcp_sdk/server

# Run MCP in dev mode
uv run mcp dev server.py
```

Then open your browser at: [http://localhost:6274](http://localhost:6274)

### 5. Start the MCP Server

**Note**: You must go to other mcp adapter frameworks folder and then go to server folder to run python file.
example:

```bash
cd src/base_mcp_sdk/server
```

From the server folder:

```bash
python server.py
# or
mcp server
```

### 6. Run the Client

**Note**: You must go to other mcp adapter frameworks folder and then go to client folder to run python file.
example:

```bash
cd src/base_mcp_sdk/client
```

Test with 3 client types: **stdio, sse, streamable-http**.

```bash
python client_sse.py
python client_stdio.py
python client_http.py
```

### 7. Test the Setup

* Ensure the **server is running** before executing a client script.
* The client will call tools and display results in the terminal.

---

## 📖 Project Overview

This project demonstrates:

* Integration of MCP with frameworks like **Google ADK, LlamaIndex, and LangChain**
* Using **MCP adapters** to interact with tools
* **Asynchronous client-server communication**

---

## 📝 Additional Notes

* Ensure the server is running before executing any client script.
* Modify `client_sse.py` (or others) to test different tools/frameworks as needed.
* Refer to the documentation of **MCP** and the integrated frameworks for advanced configurations.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Contributions are welcome! 🎉
Feel free to submit **issues** or **pull requests**.
