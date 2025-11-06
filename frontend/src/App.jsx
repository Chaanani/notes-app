import { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:4000";

function App() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const loadNotes = async () => {
    const res = await fetch(`${API_URL}/api/notes`);
    const data = await res.json();
    setNotes(data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch(`${API_URL}/api/notes`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, content }),
    });
    setTitle("");
    setContent("");
    loadNotes();
  };

  useEffect(() => {
    loadNotes();
  }, []);

  return (
    <div style={{ maxWidth: 600, margin: "0 auto", padding: 20 }}>
      <h1>Notes App</h1>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Titre"
          value={title}
          onChange={e => setTitle(e.target.value)}
        />
        <textarea
          placeholder="Contenu"
          value={content}
          onChange={e => setContent(e.target.value)}
        />
        <button type="submit">Ajouter</button>
      </form>

      <h2>Liste des notes</h2>
      <ul>
        {notes.map(n => (
          <li key={n.id}>
            <strong>{n.title}</strong><br />
            {n.content}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
