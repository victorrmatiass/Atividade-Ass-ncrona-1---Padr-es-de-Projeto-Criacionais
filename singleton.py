class DatabaseConnection:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Criando nova instância de conexão com o banco...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.status = "Conectado"
        return cls._instance

    def query(self, sql: str) -> str:
        return f"Executando query '{sql}' na instância {id(self)}"

db1 = DatabaseConnection()
print(f"Status db1: {db1.status}")

print("-" * 20)

db2 = DatabaseConnection()
print(f"Status db2: {db2.status}")

print("-" * 20)

print(f"ID do db1: {id(db1)}")
print(f"ID do db2: {id(db2)}")
print(f"db1 é o mesmo objeto que db2? {db1 is db2}")

print(db1.query("SELECT * FROM users"))
print(db2.query("SELECT * FROM products"))