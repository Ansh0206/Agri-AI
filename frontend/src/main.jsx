import React, { useMemo, useState } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

const agents = [
  {
    name: "Disease Agent",
    status: "MVP",
    accent: "green",
    input: "Crop image",
    output: "Disease probability, cause, treatment",
    metric: "92%",
  },
  {
    name: "Weather Agent",
    status: "MVP",
    accent: "blue",
    input: "Location + crop",
    output: "Rain, heat, humidity, advisory",
    metric: "3 alerts",
  },
  {
    name: "Market Agent",
    status: "MVP",
    accent: "amber",
    input: "Crop + mandi",
    output: "Price trend and selling window",
    metric: "+8.4%",
  },
  {
    name: "Voice Agent",
    status: "MVP",
    accent: "rose",
    input: "Farmer question",
    output: "Local-language advisory",
    metric: "4 langs",
  },
  {
    name: "Scheme Agent",
    status: "Phase 2",
    accent: "slate",
    input: "Scheme PDFs",
    output: "Eligibility and documents",
    metric: "RAG",
  },
  {
    name: "Pest Agent",
    status: "Phase 2",
    accent: "lime",
    input: "Season + weather",
    output: "Pest risk and prevention",
    metric: "Medium",
  },
];

const timeline = [
  "Frontend dashboard with mocked agent results",
  "FastAPI routes and orchestrator contract",
  "Disease image upload and weather risk endpoint",
  "Market trend data and voice/text advisory",
  "Scheme RAG, final report, and demo polish",
];

function App() {
  const [selectedCrop, setSelectedCrop] = useState("Tomato");
  const [question, setQuestion] = useState("My tomato leaves have yellow spots. What should I do?");
  const [language, setLanguage] = useState("English");

  const advisory = useMemo(() => {
    const crop = selectedCrop.toLowerCase();
    return {
      title: `${selectedCrop} field advisory`,
      summary:
        crop === "tomato"
          ? "Possible early blight risk. Upload a leaf photo for disease confirmation, avoid overhead watering, and check market prices before harvesting."
          : `Run disease, weather, and market agents together before making a ${crop} decision.`,
    };
  }, [selectedCrop]);

  return (
    <main className="app-shell">
      <section className="hero">
        <div className="hero-copy">
          <p className="eyebrow">Multi-agent agriculture decision system</p>
          <h1>Agri-AI Agent Console</h1>
          <p>
            A software-only farmer assistant that coordinates disease detection, weather risk,
            market pricing, voice advice, schemes, and pest planning from one workflow.
          </p>
          <div className="hero-actions">
            <button>Run Demo Advisory</button>
            <a href="#architecture">View Architecture</a>
          </div>
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
      </section>

      <section className="workspace-grid">
        <div className="panel intake-panel">
          <div className="panel-heading">
            <span>Farmer Input</span>
            <strong>Demo request</strong>
          </div>
          <label>
            Crop
            <select value={selectedCrop} onChange={(event) => setSelectedCrop(event.target.value)}>
              <option>Tomato</option>
              <option>Wheat</option>
              <option>Rice</option>
              <option>Cotton</option>
            </select>
          </label>
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
            <textarea value={question} onChange={(event) => setQuestion(event.target.value)} />
          </label>
          <div className="upload-box">
            <span>+</span>
            <p>Crop image upload area</p>
          </div>
        </div>

        <div className="panel result-panel">
          <div className="panel-heading">
            <span>Orchestrator Output</span>
            <strong>{language}</strong>
          </div>
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
      </section>

      <section className="agents-section">
        <div className="section-title">
          <p>Agent modules</p>
          <h2>Build these as independent services, then connect them through one orchestrator.</h2>
        </div>
        <div className="agent-grid">
          {agents.map((agent) => (
            <article className={`agent-card ${agent.accent}`} key={agent.name}>
              <div>
                <span>{agent.status}</span>
                <strong>{agent.metric}</strong>
              </div>
              <h3>{agent.name}</h3>
              <p>{agent.input}</p>
              <small>{agent.output}</small>
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

      <section className="timeline">
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
