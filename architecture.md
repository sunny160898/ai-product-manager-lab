# AI Product Architecture Flow

```mermaid
graph TD
    A[User / Client UI] -->|HTTP / JSON Request| B[API Gateway]
    B --> C[Backend Server / Business Logic]
    C -->|Semantic Search| D[(Vector Database / RAG)]
    C --> E[(Relational Database / SQL)]
    C --> F[LLM / AI Model Endpoint]
    F -->|Generated Response| C
    C -->|HTTP Response| A
