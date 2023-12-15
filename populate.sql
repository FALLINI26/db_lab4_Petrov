INSERT INTO users (username, first_name, last_name) VALUES
    ('user1', 'John', 'Doe'),
    ('user2', 'Jane', 'Smith'),
    ('user3', 'Bob', 'Johnson'),
    ('user4', 'Alice', 'Williams'),
    ('user5', 'Charlie', 'Brown');

INSERT INTO conversation (name) VALUES
    ('General Chat'),
    ('Team Collaboration'),
    ('Private Chat'),
    ('Project Planning'),
    ('Random Discussions');

INSERT INTO message (sender_id, conversation_id, content, timestamp) VALUES
    (1, 1, 'Hello, how is everyone?', '2023-12-15 10:00:00'),
    (2, 1, 'I''m doing well, thanks!', '2023-12-15 10:05:00'),
    (3, 2, 'Let''s discuss the project updates.', '2023-12-14 15:30:00'),
    (1, 3, 'Hey, what''s up?', '2023-12-12 08:45:00'),
    (2, 4, 'Any plans for the weekend?', '2023-12-13 12:20:00'),
    (1, 5, 'Just wanted to say hi!', '2023-12-14 09:10:00'),
    (2, 5, 'Hi there!', '2023-12-14 09:15:00'),
    (3, 1, 'Anyone free for a quick meeting?', '2023-12-15 14:00:00'),
    (4, 4, 'Let''s finalize the project timeline.', '2023-12-14 11:30:00'),
    (2, 2, 'I have some exciting news to share!', '2023-12-11 17:45:00');

INSERT INTO user_conversation (user_id, conversation_id) VALUES
    (1, 1),
    (2, 1),
    (3, 2),
    (1, 3),
    (2, 3),
    (5, 4),
    (1, 5),
    (2, 5),
    (3, 1),
    (4, 4),
    (5, 2);
