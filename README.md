# Ferm
Application for menage plants in home.

# Topology


erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses

# Build
docker build -t flask/hello-world .
docker run -p 8003:8003 flask/hello-world