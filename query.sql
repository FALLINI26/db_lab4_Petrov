select name, count(message_id) as message_count
from conversation c
    left join message m on c.conversation_id = m.conversation_id
group by name;


select username, count(message_id)
from users u
    left join message m on u.user_id = m.sender_id
group by username;


select DATE(timestamp) as date, COUNT(*) as message_count
from message
where DATE(timestamp) between '2023-12-12' and '2023-12-15'
group by DATE(timestamp)
order by DATE(timestamp);