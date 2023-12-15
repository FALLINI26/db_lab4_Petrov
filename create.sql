CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE conversation (
    conversation_id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE message (
    message_id SERIAL PRIMARY KEY,
    sender_id INT REFERENCES users(user_id),
    conversation_id INT REFERENCES conversation(conversation_id),
    content TEXT NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_conversation (
    user_id INT REFERENCES users(user_id),
    conversation_id INT REFERENCES conversation(conversation_id),
    PRIMARY KEY (user_id, conversation_id)
);
