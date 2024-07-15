import { useState, useEffect } from "react";
import ContactList from "./components/ContactList";
import "./App.css";
import ContactForm from "./components/ContactForm";

function App() {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts");
    const data = await response.json();
    setContacts(data.contacts);
    console.log(data, contacts);
  };

  return (
    <>
      <ContactList contacts={contacts} />
      <ContactForm />
    </>
  );
}

export default App;
