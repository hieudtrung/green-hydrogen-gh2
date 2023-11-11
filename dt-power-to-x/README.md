# Digital Twin for Power-to-X

Just like any other AIoT application, our system is highly IO-bounded. Some services (e.g., controller, filter, AI inference) even require real-time reaction. Furthermore, decoupling with the web console is also important to keep them working regardless of user error. Thus, I deploy them under an event-driven microservice setup.
