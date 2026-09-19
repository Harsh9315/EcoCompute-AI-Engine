# 🍃 EcoCompute AI Engine
> **Energy-Aware Green AI Benchmarking & Profiling Platform**

EcoCompute AI Engine is an enterprise-grade MLOps dashboard designed to measure, analyze, and profile real-time hardware energy consumption and carbon footprint during AI/ML model inference. Built for sustainable software engineering, it introduces **Minimum Sufficient Intelligence (MSI)** to promote Eco-Optimized model deployment.

---

## 🌟 Key Features

* **Real-time Energy Profiling:** Measures actual inference energy consumption in **Joules (J)**.
* **Live Carbon Footprint Tracking:** Automatically calculates dynamic **CO₂ emissions (g CO₂)** using grid carbon intensity logic.
* **Dynamic Eco-Grading System:**
  * ⚡ **Grade A+ (Eco-Optimized):** Triggered for lightweight architectures (e.g., MobileNet-V2).
  * ⚠️ **Grade C (Heavy Carbon):** Highlights high-energy baseline models (e.g., ResNet-18).
* **Interactive Telemetry Visualizations:** Switch between live Bar Charts and Performance Trend Lines using Chart.js.
* **Audit Execution Trail:** Complete historical log storage for execution telemetry and metric reporting.
* **CSV Data Export:** Export full benchmark execution logs for research, compliance, and academic reporting.
* **Single-Viewport Layout:** High-density, zero-scroll enterprise MLOps interface designed for Grafana/Datadog-style monitoring.

---

## 🏗️ System Architecture & Tech Stack

* **Frontend:** React.js, Chart.js, Lucide Icons, CSS3 (Dark-mode Enterprise UI)
* **Backend:** Java Spring Boot, RESTful APIs
* **ML Inference & Profiling Engine:** PyTorch, CodeCarbon Profiler Integration
* **Database:** MySQL (Execution Logs & Telemetry Audit Trail)

---

## 🚀 Getting Started

### Prerequisites
* Node.js (v16 or higher)
* Java JDK 17+
* Python 3.8+ (with PyTorch and CodeCarbon installed)
* MySQL Server

### 1. Backend Setup
```bash
# Navigate to backend folder
cd backend


### 2. Frontend Setup
Bash
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start React development server
npm start



📊 Benchmarking Workflow
Select the Target Model Architecture (e.g., ResNet-18 or MobileNet-V2).

Click Trigger Live Benchmark to initiate PyTorch profiling.

Observe real-time Energy (Joules), Latency (ms), and Carbon Emission (g CO₂) metrics.

Review updated graphs, audit execution logs, and dynamic Eco-Grade Badges.

Export benchmarking metrics via Export Report (CSV).

# Configure database in application.properties / application.yml
# Run Spring Boot Application
./mvnw spring-boot:run
