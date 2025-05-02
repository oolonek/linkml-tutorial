```mermaid
erDiagram
Container {

}
Person {
    string id  
    string full_name  
    string aliases  
    string phone  
    string age  
}

Container ||--}o Person : "persons"

```

