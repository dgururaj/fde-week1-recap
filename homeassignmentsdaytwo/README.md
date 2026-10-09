What is the difference between a Python dictionary and JSON?

Python dictionary

invoice = {
    "invoice_id": "INV-101",
    "vendor": "ABC Ltd",
    "amount": 85000,
    "status": "PENDING"
}

print(invoice["vendor"])  # ABC Ltd


-It is a Python data structure.
-You can access, add, update, and delete values.
-Its data type is dict.

JSON

{
    "invoice_id": "INV-101",
    "vendor": "ABC Ltd",
    "amount": 85000,
    "status": "PENDING"
}

-JSON stands for JavaScript Object Notation.
-It is a text format used by APIs and configuration files.
-It can be understood by many programming languages.

## Difference Between Python Dictionary and JSON

| Feature | Python Dictionary | JSON |
|---|---|---|
| Definition | A built-in Python data structure that stores key-value pairs. | A text format used to store and exchange data. |
| Data Type | `dict` | Text (`str` when represented as a Python string). |
| Keys | Can be any hashable type. | Must be strings. |
| String Quotes | Supports single or double quotes. | Requires double quotes for strings and keys. |
| Boolean Values | Uses `True` and `False`. | Uses `true` and `false`. |
| Null Values | Uses `None`. | Uses `null`. |
| Comments | Comments can be added in the surrounding Python code. | Standard JSON does not support comments. |
| Usage | Used to manipulate data within Python programs. | Used for API communication, configuration files, and data storage. |
| Conversion | Can be converted into JSON using `json.dumps()` or `json.dump()`. | Can be converted into Python objects using `json.loads()` or `json.load()`. |

### Example

**Python Dictionary:**

```python
invoice = {
    "invoice_id": "INV-101",
    "amount": 85000,
    "status": "PENDING",
    "active": True
}
```

**Equivalent JSON:**

```json
{
    "invoice_id": "INV-101",
    "amount": 85000,
    "status": "PENDING",
    "active": true
}
```

### JSON Conversion Functions

| Function | Purpose |
|---|---|
| `json.dump()` | Writes Python data to a JSON file. |
| `json.load()` | Reads JSON data from a file into Python objects. |
| `json.dumps()` | Converts Python data into a JSON string. |
| `json.loads()` | Converts a JSON string into Python objects. |

**Key Takeaway:** A Python dictionary is a data structure used to work with data in Python, whereas JSON is a text format used to exchange or store data across applications.



### What Does `json.load()` Do?

`json.load()` reads JSON data from a file and converts it into Python objects, such as a list or dictionary.

### What Does `json.dump()` Do?

`json.dump()` writes Python data, such as a list or dictionary, into a JSON file.


## Why Does In-Memory Data Disappear After Restarting Uvicorn?

In-memory data disappears after restarting Uvicorn because it is stored in the application's RAM rather than in permanent storage.

### 1. How In-Memory Storage Works

Consider the following example:

```python
from fastapi import FastAPI

app = FastAPI()

invoices = [
    {"invoice_id": "INV-101", "amount": 85000}
]

@app.get("/invoices")
def get_invoices():
    return invoices
```

- The `invoices` list is stored in the application's memory (RAM).
- When a new invoice is added, it exists only in memory.
- When Uvicorn restarts, the previous Python process terminates and its memory is released.
- A new Python process starts, and the `invoices` list is initialized again with its original values.

### 2. What Happens When Uvicorn Restarts?

1. **Application starts:** The Python list is initialized in memory.
2. **Data is added:** New invoice records are added to the list.
3. **Uvicorn restarts:** The existing application process terminates, and its in-memory data is lost.
4. **Application starts again:** The list is recreated with its initial values.

### 3. How to Prevent Data Loss

| Storage Type | Data Persists After Restart? | Use Case |
|---|---|---|
| Python list or dictionary | No | Learning and temporary data |
| JSON file | Yes | Small projects and demonstrations |
| SQLite database | Yes | Small applications and local development |
| PostgreSQL database | Yes | Applications requiring reliable persistent storage |

### 4. Recommended Approach

For a simple FastAPI invoice project, a JSON file can be used to persist data between restarts.

- Use `json.load()` to read existing invoice records from a JSON file.
- Use `json.dump()` to save updated invoice records to the file.

For production applications, use a database such as PostgreSQL to provide more reliable storage and handle concurrent requests safely.

### Key Takeaway

**In-memory storage is temporary, whereas files and databases provide persistent storage.** Restarting Uvicorn recreates the application's memory, so any data that was not saved to persistent storage is lost.


## Why Might We Eventually Replace a JSON File with PostgreSQL?

A JSON file is useful for learning and building small applications. However, as the application grows, PostgreSQL provides better data management, reliability, and scalability.

### 1. Limitations of a JSON File

- **Concurrent access:** Multiple API requests writing to the same JSON file can overwrite each other's changes or cause data inconsistencies.
- **Data integrity:** JSON files do not enforce database constraints, such as unique invoice IDs or required relationships between records.
- **Querying data:** Filtering, sorting, and aggregating large amounts of data is less efficient and convenient than using SQL queries.
- **Scalability:** Reading and rewriting an entire JSON file becomes inefficient as the number of invoice records increases.
- **Transactions:** JSON files do not provide built-in database transactions to ensure that a group of operations succeeds or fails together.
- **Data relationships:** Managing relationships between invoices, vendors, and payments becomes difficult as the application grows.
- **Multi-user access:** A database is better suited to serving multiple users and application instances concurrently.

### 2. JSON File vs PostgreSQL

| Feature | JSON File | PostgreSQL |
|---|---|---|
| Storage | File-based | Relational database |
| Data persistence | Yes, when saved to disk | Yes, when committed to the database |
| Concurrent writes | Requires manual coordination | Supports concurrent transactions |
| Data validation | Primarily application-managed | Supports constraints and data types |
| Querying | Python code required | SQL queries |
| Transactions | No built-in database transactions | Supports ACID transactions |
| Relationships | Managed manually | Supports foreign keys and joins |
| Scalability | Suitable for small datasets | Better suited to growing datasets and workloads |
| Best use case | Learning, prototypes, simple demos | Production applications and structured business data |

### 3. Example: Invoice Management

With a JSON file, retrieving all pending invoices might require loading the file and filtering the records in Python.

```python
pending_invoices = [
    invoice for invoice in invoices
    if invoice["status"] == "PENDING"
]
```

With PostgreSQL, the same operation can be performed using SQL:

```sql
SELECT *
FROM invoices
WHERE status = 'PENDING';
```

PostgreSQL can use indexes to improve query performance as the dataset grows.

### 4. When Should We Switch to PostgreSQL?

Consider replacing JSON storage when:

- The application has many invoice records.
- Multiple users or API requests may create or update invoices simultaneously.
- You need reliable transactions and data integrity.
- You need complex filtering, reporting, or aggregations.
- You need relationships between invoices, vendors, and payments.
- The application is moving toward production deployment.

### Key Takeaway

**JSON files are suitable for simple prototypes, while PostgreSQL is better suited to reliable, multi-user applications that require structured data, concurrent access, transactions, and efficient querying.**