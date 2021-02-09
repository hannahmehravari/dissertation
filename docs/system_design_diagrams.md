# System Design Diagrams
## Version 1
```mermaid
%% YOU NEED A MERMAID MARKDOWN PLUGIN TO RENDER THIS DIAGRAM 
sequenceDiagram
    participant Turbine Mounted Sensors
    participant SMARTStop
    par Collect New Training Data
    loop Predefined sample rate
    ML API->>SMARTStop: Request Wind Speed/Direction Sample
    SMARTStop->>Turbine Mounted Sensors:Request Turbine Data
    Turbine Mounted Sensors->>SMARTStop: Return Turbine Data
    SMARTStop->>ML API: Return Wind Speed/Direction Sample
    ML API ->> Training Set: New wind Speed/Direction sample
    end
    and Retrain and Replace Active Forecasting Model
    ML API->>+Wind Speed/Direction Training Module:Request Newly Trained Model
    Wind Speed/Direction Training Module->>Training Set:Request New Training Data
    Training Set->>Wind Speed/Direction Training Module: Return New Training Data
    Wind Speed/Direction Training Module->>Forecasting Model: Request Newly Trained Model
    Forecasting Model->>Wind Speed/Direction Training Module: Return Newly Trained Model
    Wind Speed/Direction Training Module->> ML API: Return Newly Trained Model
    and Plan Turbine Stops
    loop every time active forecasting model is replaced
    SMARTStop->>ML API:Request Turbine Statuses
    ML API->> Forecasting Model: Request Prediction
    Forecasting Model->>ML API:Return Prediction
    ML API->> Noise Campaign Histogram: Request remaining bins to complete
    Noise Campaign Histogram->>ML API: Return remaining bins to complete
    ML API ->> SMARTStop: Return Turbine Statuses
    end
    and Fill in Histogram with Measurements
    loop for every planned turbine start/pause
    ML API->> SMARTStop: Request required noise measurements
    SMARTStop->>Turbine Mounted Sensors:Request Noise Measurements
    Turbine Mounted Sensors->> SMARTStop: Return Noise Measurements
    SMARTStop ->>ML API: Return required noise measurements
    ML API ->> Noise Campaign Histogram: Fill in required bins
    end
    end
```

## Version 2

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