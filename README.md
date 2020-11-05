# Proactive and Reactive Decision Making Over Wind Turbine Time Series Data

## System Overview
```mermaid
%% YOU NEED A MERMAID MARKDOWN PLUGIN TO RENDER THIS DIAGRAM 
sequenceDiagram
    participant Turbine Mounted Sensors
    participant SMARTStop
    par Collect New Training Data
    loop Predefined sample rate
    ML API->>SMARTStop: Request Wind Speed Sample
    SMARTStop->>Turbine Mounted Sensors:Request Turbine Data
    Turbine Mounted Sensors->>SMARTStop: Return Turbine Data
    SMARTStop->>ML API: Return Wind Speed Sample
    ML API ->> Training Set: New wind speed sample
    end
    and Retrain and Replace Active Forecasting Model
    ML API->>+Wind Speed Training Module:Request Newly Trained Model
    Wind Speed Training Module->>Training Set:Request New Training Data
    Training Set->>Wind Speed Training Module: Return New Training Data
    Wind Speed Training Module->>Forecasting Model: Request Newly Trained Model
    Forecasting Model->>Wind Speed Training Module: Return Newly Trained Model
    Wind Speed Training Module->> ML API: Return Newly Trained Model
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

## Resouces
Data: https://drive.google.com/drive/folders/1OxU2EAok-bl-nMdh3CevdV7jY4nMOJ7Q?usp=sharing

Task tracker: https://github.com/hannahmehravari/dissertation/projects/1
