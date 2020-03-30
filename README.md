# Agent-Based Modelling for Hospital Resource Allocation in Viral Crises

This is a <b>school project</b>, and a <b>work-in-progress</b> to understand resource allocations, policy interventions and the extent to which they influence transmission in a building structure. It is currently a baseline experiment <b>without any reference to current research</b> on COVID-19, but stay tuned!

<img src="https://user-images.githubusercontent.com/27071473/77895747-cea23d80-72a9-11ea-99c6-582c7c6db101.png" width="50%">
<img src="https://user-images.githubusercontent.com/27071473/77895604-9c90db80-72a9-11ea-929d-b129a3af7e82.png" width="50%">

## Context

In viral crises such as the current COVID-19 situation, resources are limited in hospitals, such as hospital beds and staff. To exacerbate the situation, viruses can be transmitted as patients move from one station in the hospital to another.

## Objective

To explore an optimal and safer allocation of hospital resources and staff that maximises rate of patient recovery while minimising rate of patient viral transmission.

## Methodology

We plan to create a simulation of hospital operations. Hospital processes are modeled as Dynamical Systems where the rates of waiting times or time required for processes can be adjusted according to the particular hospital. Patients and staff can be modeled using Agent-Based Modeling (ABM) with varying rates of transmission of viral infection.

## Baseline Experiment Results

### Transmission rate vs Transmission count

<img src="https://user-images.githubusercontent.com/27071473/77892667-8a14a300-72a5-11ea-8740-db65e91f0474.png" width="50%">

### Time spent in pharmacy vs Transmission count

<img src="https://user-images.githubusercontent.com/27071473/77892684-8ed95700-72a5-11ea-962f-0d010b04dd6f.png" width="50%">

### Time spent in waiting area vs Transmission count

<img src="https://user-images.githubusercontent.com/27071473/77892651-86811c00-72a5-11ea-8dd0-ccfdc28ad320.png" width="50%">

### Experiment Parameters
* Time spent in entrance: 10
* Time spent in pharmacy: 15
* Time spent in registration: 20
* Time spent in waiting area: 60
* Size of entrance: (20,10)
* Size of pharmacy: (8,8)
* Size of registration: (5,5)
* Size of waiting area: (10,10)
* Probability of patient arrival: 0.1
* Probability of infected patient arrival: 0.1
* Probability of transmission on contact: 0.1

### Experiment Hyperparameters
* No. of experiments per set of parameters: 100
* No. of epochs per experiment: 1000
