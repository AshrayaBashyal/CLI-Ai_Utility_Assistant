
# In-memory mock contacts database
CONTACTS = [
    {"name": "John Smith", "email": "john.smith@gmail.com"},
    {"name": "John Doe", "email": "john.doe@gmail.com"},
    {"name": "Alice Brown", "email": "alice@gmail.com"}
]

def get_contact(name: str) -> dict:
    try:
        search_query = str(name).lower().strip()
        
        # Guard clause for empty strings
        if not search_query:
            return {"success": False, "error": {"message": "Search name cannot be empty."}}
            
        # Find all contacts where search_query is a substring of the name
        matches = [c for c in CONTACTS if search_query in c["name"].lower()]
        
        if not matches:
            return {"success": False, "error": {"message": "Contact not found."}}
            
        return {
            "success": True,
            "data": {
                "matches": matches
            }
        }
    except Exception as e:
        return {"success": False, "error": {"message": str(e)}}
