# Proactive and Reactive Decision Making Over Wind Turbine Time Series Data

## How to Run
in the root directory, run:
```
docker-compose build
docker-compose up
```

API is hosted on `localhost:5000`
Database is hosted on `localhost:8086`


## System Overview

### AutoML API
```mermaid
sequenceDiagram
    participant Database
    participant Sampler
    participant Joiner
    participant Trainer
    participant Predictor
    participant Data Monitoring
    participant Prediction Monitoring
    participant Business Logic
    participant Model Policy Engine
    par Prediction Monitoring
    Database->>Sampler:Wind Data
    Sampler->>Joiner:Sample 
    Joiner->>Predictor:Sample Transformed to Required Format
    Note over Predictor, Prediction Monitoring: To compare predictions to real life wind events
    Predictor->>Prediction Monitoring:Predictions
    par Hypervisor
    Note over Database, Trainer: Self-Correction: Determining whether or not the model should be retrained
    Database->>Sampler:Wind Data
    Sampler->>Joiner:Sample 
    Joiner->>Data Monitoring:Sample Transformed to Required Format
    Note over Data Monitoring,Business Logic: Self-Diagnosis
    Data Monitoring->>Model Policy Engine:Data Statistics (Possible Anomalies, Drift, and Change-Points)
    Prediction Monitoring->>Model Policy Engine:Prediction Statistics   
    Business Logic->>Model Policy Engine: Business Metrics
    alt If Prediction Error > Limit
    Database->>Sampler:Wind Data
    Sampler->>Joiner:Sample 
    Joiner->>Trainer:Sample Transformed to Required Format
    Trainer->>Predictor: Replace Predictor
    end
    end
    end
```

### Turbine Curtailment
```mermaid
sequenceDiagram
    participant SpeedxDirection Histogram
    participant AutoML API
    participant Campaign Runner
    participant Future Turbine Status Queue
    participant SMARTStop
    SpeedxDirection Histogram->>Campaign Runner: Remaining Measurements to be taken
    AutoML API->>Campaign Runner:Upcoming Wind Speeds and Directions
    Note over Campaign Runner,Future Turbine Status Queue: if required wind event upcoming
    Campaign Runner->>Future Turbine Status Queue: Schedule Turbine Status Change 
    Future Turbine Status Queue->>SMARTStop: Turbine Status

```

### Maintaining Training Set
```mermaid
sequenceDiagram
    participant SMARTStop
    participant Data Streamer
    participant Database
    SMARTStop->>Data Streamer:Wind Speed and Wind Direction Data
    Data Streamer->>Database:New Entry to training/validation data
```

## Resouces
Data: https://drive.google.com/drive/folders/1OxU2EAok-bl-nMdh3CevdV7jY4nMOJ7Q?usp=sharing

Task tracker: https://github.com/hannahmehravari/dissertation/projects/1
