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

const executionSteps = [
  {
    agent: "Disease Agent",
    task: "Analyze symptom text and crop image input",
    file: "services/disease_agent.py",
  },
  {
    agent: "Weather Agent",
    task: "Check district-level weather risk",
    file: "services/weather_agent.py",
  },
  {
    agent: "Market Agent",
    task: "Estimate mandi price signal",
    file: "services/market_agent.py",
  },
  {
    agent: "Orchestrator",
    task: "Merge agent outputs into one advisory",
    file: "orchestrator.py",
  },
];

function App() {
  const [selectedCrop, setSelectedCrop] = useState("Tomato");
  const [district, setDistrict] = useState("Nashik");
  const [language, setLanguage] = useState("English");
  const [question, setQuestion] = useState("My tomato leaves have yellow spots. What should I do?");
  const [advisoryResponse, setAdvisoryResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const fallbackAdvisory = useMemo(() => {
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

  const advisory = advisoryResponse
    ? {
        title: `${advisoryResponse.crop} advisory for ${advisoryResponse.district}`,
        confidence: `${Math.round(advisoryResponse.overall_confidence * 100)}%`,
        summary: advisoryResponse.summary,
      }
    : fallbackAdvisory;

  const recommendations = advisoryResponse?.recommendations ?? [
    {
      title: "Next action",
      detail: "Upload image and verify symptoms",
      priority: "high",
    },
    {
      title: "Market signal",
      detail: "Hold for 2-3 days if storage is available",
      priority: "medium",
    },
    {
      title: "Weather risk",
      detail: "High humidity tomorrow evening",
      priority: "medium",
    },
  ];

  const completedAgents = new Set(advisoryResponse?.agent_results.map((result) => result.agent) ?? []);

  async function generateAdvisory() {
    setIsLoading(true);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/advisory", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          crop: selectedCrop,
          district,
          language,
          question,
        }),
      });

      if (!response.ok) {
        throw new Error("Backend returned an error. Check FastAPI terminal.");
      }

      const data = await response.json();
      setAdvisoryResponse(data);
    } catch (apiError) {
      setError(
        apiError instanceof Error
          ? apiError.message
          : "Could not connect to backend. Make sure FastAPI is running on port 8000.",
      );
    } finally {
      setIsLoading(false);
    }
  }

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
              <textarea value={question} onChange={(event) => setQuestion(event.target.value)} />
            </label>
            <div className="upload-box">
              <span>+</span>
              <p>Upload crop image for disease detection</p>
              <small>JPG, PNG, or phone camera image</small>
            </div>
            <button className="generate-button" type="button" onClick={generateAdvisory} disabled={isLoading}>
              {isLoading ? "Calling FastAPI..." : "Generate Advisory"}
            </button>
            {error && <p className="error-message">{error}</p>}
          </div>

          <div className="panel result-panel">
            <div className="panel-heading">
              <span>Orchestrator Output</span>
              <strong>{advisoryResponse ? "Connected to backend" : language}</strong>
            </div>
            <div className="confidence-pill">{advisory.confidence} confidence</div>
            <h2>{advisory.title}</h2>
            <p>{advisory.summary}</p>
            <div className="recommendations">
              {recommendations.map((recommendation) => (
                <div key={recommendation.title}>
                  <span>{recommendation.title}</span>
                  <strong>{recommendation.detail}</strong>
                  {recommendation.priority && <small>{recommendation.priority} priority</small>}
                </div>
              ))}
            </div>
            {advisoryResponse && (
              <div className="agent-results">
                <span>Agent responses from FastAPI</span>
                {advisoryResponse.agent_results.map((result) => (
                  <article key={result.agent}>
                    <strong>{result.agent}</strong>
                    <p>{result.summary}</p>
                    <small>{Math.round(result.confidence * 100)}% confidence</small>
                  </article>
                ))}
              </div>
            )}
          </div>
        </div>

        <div className="execution-panel">
          <div className="panel-heading">
            <span>Agent Execution Timeline</span>
            <strong>{advisoryResponse ? "Completed" : isLoading ? "Running" : "Waiting"}</strong>
          </div>
          <div className="execution-steps">
            {executionSteps.map((step, index) => {
              const isComplete = step.agent === "Orchestrator" ? Boolean(advisoryResponse) : completedAgents.has(step.agent);
              const status = isComplete ? "complete" : isLoading ? "running" : "pending";

              return (
                <article className={`execution-step ${status}`} key={step.agent}>
                  <div className="step-index">{String(index + 1).padStart(2, "0")}</div>
                  <div>
                    <span>{status}</span>
                    <h3>{step.agent}</h3>
                    <p>{step.task}</p>
                    <small>{step.file}</small>
                  </div>
                </article>
              );
            })}
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
