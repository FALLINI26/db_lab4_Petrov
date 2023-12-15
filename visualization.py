import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter

from main import StatisticsProvider


class StatisticsVisualizer:
    def __init__(self):
        self.statistics_provider = StatisticsProvider()

    def showHistogram(self):
        conversation_messages_count = self.statistics_provider.get_conversation_messages_count()
        conversation_names, message_counts = zip(*conversation_messages_count)

        plt.figure(figsize=(11, 6))
        plt.bar(conversation_names, message_counts, color='lightblue')
        plt.title('Message count for conversations')
        plt.show()

    def showCircleDiagram(self):
        user_messages_count = self.statistics_provider.get_user_messages_count()
        usernames, message_counts = zip(*user_messages_count)

        plt.pie(message_counts, labels=usernames, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        plt.title('Message percentage for users')
        plt.show()

    def showGraph(self):
        daily_messages_count = self.statistics_provider.get_daily_messages_count()
        dates, message_counts = zip(*daily_messages_count)

        plt.plot(dates, message_counts)
        plt.xlabel('Solves')
        plt.ylabel('Time (seconds)')
        plt.title('Daily message count')

        plt.gca().xaxis.set_major_formatter(DateFormatter('%d.%m.%y'))
        plt.gca().xaxis.set_major_locator(DayLocator())
        plt.ylim(bottom=0)

        plt.show()


statistics_visualizer = StatisticsVisualizer()
statistics_visualizer.showHistogram()
statistics_visualizer.showCircleDiagram()
statistics_visualizer.showGraph()
