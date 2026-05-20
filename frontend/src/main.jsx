import React, { useMemo, useState } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

const agents = [
  {
    name: "Disease Agent",
    status: "Ready",
    accent: "green",
    input: "Crop image",
    output: "Disease probability, cause, treatment",
    metric: "92%",
    detail: "Vision model + farmer-safe explanation",
  },
  {
    name: "Weather Agent",
    status: "Ready",
    accent: "blue",
    input: "Location + crop",
    output: "Rain, heat, humidity, advisory",
    metric: "3 alerts",
    detail: "Weather forecast converted into farm actions",
  },
  {
    name: "Market Agent",
    status: "Ready",
    accent: "amber",
    input: "Crop + mandi",
    output: "Price trend and selling window",
    metric: "+8.4%",
    detail: "Mandi trend signal for selling decisions",
  },
  {
    name: "Voice Agent",
    status: "Ready",
    accent: "rose",
    input: "Farmer question",
    output: "Local-language advisory",
    metric: "4 langs",
    detail: "Text now, speech integration next",
  },
  {
    name: "Scheme Agent",
    status: "Next",
    accent: "slate",
    input: "Scheme PDFs",
    output: "Eligibility and documents",
    metric: "RAG",
    detail: "PDF search for subsidies and insurance",
  },
  {
    name: "Pest Agent",
    status: "Next",
    accent: "lime",
    input: "Season + weather",
    output: "Pest risk and prevention",
    metric: "Medium",
    detail: "Risk scoring from season and weather",
  },
];

const stats = [
  ["4", "MVP agents"],
  ["7", "Total planned agents"],
  ["0", "Hardware modules"],
  ["10 Jun", "Submission target"],
];

const timeline = [
  "Polished frontend dashboard and project walkthrough",
  "FastAPI routes with mocked agent responses",
  "Disease image upload and weather risk endpoint",
  "Market trend data and local-language advisory",
  "Final report, screenshots, and demo video",
];

function App() {
  const [selectedCrop, setSelectedCrop] = useState("Tomato");
  const [district, setDistrict] = useState("Nashik");
  const [language, setLanguage] = useState("English");

  const advisory = useMemo(() => {
    const crop = selectedCrop.toLowerCase();
    return {
      title: `${selectedCrop} advisory for ${district}`,
      confidence: crop === "tomato" ? "86%" : "78%",
      summary:
        crop === "tomato"
          ? "Possible early blight risk. Upload a leaf photo for confirmation, avoid overhead watering, and check mandi prices before harvesting."
          : `Run disease, weather, and market agents together before making a ${crop} decision in ${district}.`,
    };
  }, [district, selectedCrop]);

  return (
    <main className="app-shell">
      <nav className="topbar">
        <a className="brand" href="#top">
          <span>AI</span>
          <strong>Agri-AI</strong>
        </a>
        <div className="nav-links">
          <a href="#dashboard">Dashboard</a>
          <a href="#agents">Agents</a>
          <a href="#architecture">Architecture</a>
          <a href="#timeline">Plan</a>
        </div>
      </nav>

      <section className="hero" id="top">
        <div className="hero-copy">
          <p className="eyebrow">Multi-agent agriculture decision system</p>
          <h1>Farmer Decision Dashboard</h1>
          <p>
            A software-only demo console for crop disease detection, weather risk, mandi price
            guidance, voice advice, scheme discovery, and pest planning.
          </p>
          <div className="hero-actions">
            <a className="primary-action" href="#dashboard">Open Demo Dashboard</a>
            <a href="#architecture">View Architecture</a>
          </div>
          <div className="stat-strip">
            {stats.map(([value, label]) => (
              <div key={label}>
                <strong>{value}</strong>
                <span>{label}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="mission-card">
          <div className="mission-header">
            <span>Live farm snapshot</span>
            <strong>Demo mode</strong>
          </div>
          <div className="field-visual" aria-label="stylized crop monitoring panel">
            <div className="sun" />
            <div className="scan-line" />
            <div className="field-row row-a" />
            <div className="field-row row-b" />
            <div className="field-row row-c" />
            <div className="sensor-card">
              <span>Disease risk</span>
              <strong>Low to medium</strong>
            </div>
          </div>
          <div className="mission-footer">
            <div>
              <span>Weather</span>
              <strong>Humid evening</strong>
            </div>
            <div>
              <span>Market</span>
              <strong>Price rising</strong>
            </div>
          </div>
        </div>
      </section>

      <section className="dashboard" id="dashboard">
        <div className="section-title">
          <p>Demo workspace</p>
          <h2>One farmer request, multiple agents, one clear advisory.</h2>
        </div>

        <div className="workspace-grid">
          <div className="panel intake-panel">
            <div className="panel-heading">
              <span>Farmer Input</span>
              <strong>Request builder</strong>
            </div>
            <div className="form-grid">
              <label>
                Crop
                <select value={selectedCrop} onChange={(event) => setSelectedCrop(event.target.value)}>
                  <option>Tomato</option>
                  <option>Wheat</option>
                  <option>Rice</option>
                  <option>Cotton</option>
                  <option>Onion</option>
                </select>
              </label>
              <label>
                District
                <select value={district} onChange={(event) => setDistrict(event.target.value)}>
                  <option>Nashik</option>
                  <option>Pune</option>
                  <option>Indore</option>
                  <option>Ludhiana</option>
                  <option>Guntur</option>
                </select>
              </label>
            </div>
            <label>
              Language
              <select value={language} onChange={(event) => setLanguage(event.target.value)}>
                <option>English</option>
                <option>Hindi</option>
                <option>Marathi</option>
                <option>Tamil</option>
              </select>
            </label>
            <label>
              Farmer question
              <textarea defaultValue="My tomato leaves have yellow spots. What should I do?" />
            </label>
            <div className="upload-box">
              <span>+</span>
              <p>Upload crop image for disease detection</p>
              <small>JPG, PNG, or phone camera image</small>
            </div>
          </div>

          <div className="panel result-panel">
            <div className="panel-heading">
              <span>Orchestrator Output</span>
              <strong>{language}</strong>
            </div>
            <div className="confidence-pill">{advisory.confidence} confidence</div>
            <h2>{advisory.title}</h2>
            <p>{advisory.summary}</p>
            <div className="recommendations">
              <div>
                <span>Next action</span>
                <strong>Upload image and verify symptoms</strong>
              </div>
              <div>
                <span>Market signal</span>
                <strong>Hold for 2-3 days if storage is available</strong>
              </div>
              <div>
                <span>Weather risk</span>
                <strong>High humidity tomorrow evening</strong>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="agents-section" id="agents">
        <div className="section-title">
          <p>Agent modules</p>
          <h2>Specialized agents that can be built and tested independently.</h2>
        </div>
        <div className="agent-grid">
          {agents.map((agent) => (
            <article className={`agent-card ${agent.accent}`} key={agent.name}>
              <div className="agent-topline">
                <span>{agent.status}</span>
                <strong>{agent.metric}</strong>
              </div>
              <h3>{agent.name}</h3>
              <p>{agent.input}</p>
              <small>{agent.output}</small>
              <em>{agent.detail}</em>
            </article>
          ))}
        </div>
      </section>

      <section className="architecture" id="architecture">
        <div className="section-title">
          <p>Architecture</p>
          <h2>Software-only system, no irrigation hardware required.</h2>
        </div>
        <div className="flow">
          {["React frontend", "FastAPI backend", "Agent orchestrator", "Specialized agents", "Shared AI + data layer"].map(
            (step, index) => (
              <div className="flow-step" key={step}>
                <span>{String(index + 1).padStart(2, "0")}</span>
                <strong>{step}</strong>
              </div>
            ),
          )}
        </div>
      </section>

      <section className="timeline" id="timeline">
        <div className="section-title">
          <p>Build path</p>
          <h2>What you can finish before June 10.</h2>
        </div>
        <ol>
          {timeline.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ol>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
