graph TD
    subgraph User Clients
        WebApp[Web Application <br/> (React/Vue/Angular)]
        MobileApp[Mobile Application <br/> (Native/Flutter/React Native)]
    end

    subgraph External Systems
        BrokerAPIs[Broker APIs <br/> (Delta.xchange, Binance, etc.)]
        PaymentGW[Payment Gateways]
        MarketDataFeeds[External Market Data Feeds]
    end

    APIGateway[API Gateway <br/> (e.g., Kong, Traefik, Nginx) <br/> AuthN/AuthZ, Rate Limiting, Routing <br/> Exposes REST/GraphQL]

    WebApp --> APIGateway
    MobileApp --> APIGateway

    MessageBus[Central Message Bus <br/> (e.g., Kafka / NATS / RabbitMQ) <br/> Events: MarketData, OrderSignals, TradeConfirmations, Alerts]

    subgraph Backend Microservices (e.g., written in Go)
        UserSvc[User & Account Service <br/> (REST/gRPC)]
        StrategyMgmtSvc[Strategy Mgmt & Backtesting Service <br/> (REST/gRPC)]
        MarketDataIngSvc[Market Data Ingestion Service <br/> (Connects to Feeds/Brokers, Publishes to MessageBus)]
        TradingEngineSvc[Trading Engine Service <br/> (Consumes MarketData, Evaluates Strategies, Publishes OrderSignals)]
        OrderOrchSvc[Order Orchestration & Broker Integration Service <br/> (Consumes OrderSignals, Interacts with BrokerAPIs, Publishes TradeConfirmations)]
        PortfolioPnLSvc[Portfolio & P&L Service <br/> (Consumes TradeConfirmations, Calculates P&L, Exposes via API)]
        NotificationSvc[Notification Service <br/> (Consumes AlertEvents, Sends Email/SMS/Push)]
        PaymentSubSvc[Payment & Subscription Service <br/> (REST/gRPC, Integrates with PaymentGW)]
        BackofficeSvc[Backoffice & Reporting Service <br/> (REST/gRPC)]
    end

    APIGateway -- REST/GraphQL --> UserSvc
    APIGateway -- REST/GraphQL --> StrategyMgmtSvc
    APIGateway -- REST/GraphQL --> PortfolioPnLSvc
    APIGateway -- REST/GraphQL --> PaymentSubSvc
    APIGateway -- REST/GraphQL --> BackofficeSvc

    MarketDataIngSvc -- Fetches Data --> BrokerAPIs
    MarketDataIngSvc -- Fetches Data --> MarketDataFeeds
    MarketDataIngSvc -- Publishes Market Data Ticks/Candles --> MessageBus

    TradingEngineSvc -- Subscribes to Market Data --> MessageBus
    TradingEngineSvc -- Publishes Order Signals --> MessageBus
    TradingEngineSvc -- Reads Strategy Config --> StrategyDB

    OrderOrchSvc -- Subscribes to Order Signals --> MessageBus
    OrderOrchSvc -- Places Orders / Gets Status --> BrokerAPIs
    OrderOrchSvc -- Publishes Trade Confirmations/Status --> MessageBus

    PortfolioPnLSvc -- Subscribes to Trade Confirmations --> MessageBus
    PortfolioPnLSvc -- Reads Account Info --> UserDB
    PortfolioPnLSvc -- Reads Market Data for Valuation --> MarketDataDB

    NotificationSvc -- Subscribes to Alert Events (from MessageBus or direct gRPC) --> MessageBus
    NotificationSvc -- Sends Notifications --> UserSvc // (to get contact details) & External (Email/SMS GW)

    PaymentSubSvc --> PaymentGW
    PaymentSubSvc --> UserDB

    UserSvc --> UserDB
    StrategyMgmtSvc --> StrategyDB
    StrategyMgmtSvc --> MarketDataDB // For backtesting data
    MarketDataIngSvc --> MarketDataDB
    OrderOrchSvc --> TradeDB
    PortfolioPnLSvc --> TradeDB // Also for P&L calculation records
    BackofficeSvc --> UserDB
    BackofficeSvc --> StrategyDB
    BackofficeSvc --> TradeDB

    subgraph Data Stores (Polyglot Persistence)
        UserDB[(User DB <br/> e.g., CockroachDB/PostgreSQL)]
        StrategyDB[(Strategy DB <br/> e.g., PostgreSQL/MongoDB)]
        MarketDataDB[(Time-Series Market Data DB <br/> e.g., TimescaleDB/InfluxDB)]
        TradeDB[(Trade & Position DB <br/> e.g., CockroachDB/PostgreSQL)]
        Cache[(Distributed Cache <br/> e.g., Redis Cluster)]
    end

    UserSvc --> Cache
    StrategyMgmtSvc --> Cache
    TradingEngineSvc --> Cache // For hot strategies/market data snapshots
    PortfolioPnLSvc --> Cache // For live P&L

    subgraph Observability
        Logging[Centralized Logging <br/> (ELK Stack / Grafana Loki)]
        Metrics[Metrics Collection & Visualization <br/> (Prometheus, Grafana)]
        Tracing[Distributed Tracing <br/> (Jaeger / Zipkin)]
        Alerting[Alerting System <br/> (Alertmanager)]
    end

    BackendMicroservices -- Telemetry Data (Logs, Metrics, Traces) --> Observability
    APIGateway -- Telemetry Data --> Observability
    Observability -- Alerts --> NotificationSvc

    style APIGateway fill:#lightblue,stroke:#333,stroke-width:2px
    style MessageBus fill:#lightgrey,stroke:#333,stroke-width:2px
    style UserSvc fill:#bbf,stroke:#333,stroke-width:2px
    style StrategyMgmtSvc fill:#bbf,stroke:#333,stroke-width:2px
    style MarketDataIngSvc fill:#f9f,stroke:#333,stroke-width:2px,labelStyle:"font-weight:bold"
    style TradingEngineSvc fill:#f9f,stroke:#333,stroke-width:2px,labelStyle:"font-weight:bold"
    style OrderOrchSvc fill:#f9f,stroke:#333,stroke-width:2px,labelStyle:"font-weight:bold"
    style PortfolioPnLSvc fill:#bbf,stroke:#333,stroke-width:2px
    style NotificationSvc fill:#bbf,stroke:#333,stroke-width:2px
    style PaymentSubSvc fill:#bbf,stroke:#333,stroke-width:2px
    style BackofficeSvc fill:#bbf,stroke:#333,stroke-width:2px
    style MarketDataDB fill:#ccf,stroke:#333,stroke-width:2px
    style TradeDB fill:#ccf,stroke:#333,stroke-width:2px
    style UserDB fill:#ccf,stroke:#333,stroke-width:2px
    style StrategyDB fill:#ccf,stroke:#333,stroke-width:2px
    style Cache fill:#ccf,stroke:#333,stroke-width:2px
