from collections import Counter
class SocialNetwork:
    def __init__(self):
        self.network = {}

    def load_network(self, file_name):
        try:
            with open(file_name, 'r') as file:
                num_members = int(file.readline().strip())
                for i in range(num_members):
                    line = file.readline().strip().split()
                    friend1, friend2 = line[0], line[1]
                    if friend1 not in self.network:
                        self.network[friend1] = []
                    if friend2 not in self.network:
                        self.network[friend2] = []
                    self.network[friend1].append(friend2)
                    self.network[friend2].append(frienå1)
            print("File opened successfully")
            return True
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")
            return False

    def display_network(self):
from collections import Counter

# Define the SocialNetwork class
class SocialNetwork:
    def __init__(self):
        self.network = {}

    def load_network(self, file_name):
        try:
            with open(file_name, 'r') as file:
                num_members = int(file.readline().strip())
                for i in range(num_members):
                    line = file.readline().strip().split()
                    friend1, friend2 = line[0], line[1]
                    if friend1 not in self.network:
                        self.network[friend1] = []
                    if friend2 not in self.network:
                        self.network[friend2] = []
                    self.network[friend1].append(friend2)
                    self.network[friend2].append(friend1)
            print("File opened successfully")
            return True
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")
            return False

    def display_network(self):
        print("Social Network:")
        for friend1 in self.network:
            friends = ', '.join(self.network[friend1])
            print(f"{friend1} -> {friends}")

# Define the Friendship class
class Friendship:
    def __init__(self, network):
        self.network = network
        self.friend_count = {}
        self.recommendations = {}

    def count_friends(self):
        # Count common friends for each user
        self.friend_count = {user: sum(1 for friend in friends if friend != user) for user, friends in self.network.items()}

    def display_friend_count(self):
        self.count_friends()
        print("Common Friend Count:")
        for friend, count in self.friend_count.items():
            print(f"{friend}: {count}")

    # ... (rest of the methods)

if __name__ == "__main__":
    sn = SocialNetwork()
    friendship = Friendship(sn.network)

    while True:
        file_name = input("Enter file name or type 'n' to exit: ")
        if file_name == "n":
            break
        success = sn.load_network(file_name)
        if success:
            display_network = input("Do you want to display the network? (y/n) ")
            if display_network == "y":
                sn.display_network()

            display_friend_count = input("Do you want to display the common friend count? (y/n) ")
            if display_friend_count == "y":
                friendship.display_friend_count()

                recommend_friend = "y"
                while recommend_friend == "y":
                    user = input("Enter the user name to recommend friends: ")
                    friendship.recommend_friend(user)
                    recommend_friend = input("Do you want to recommend friends for another user? (y/n) ")

                display_num_friends = "y"
                while display_num_friends == "y":
                    user = input("Enter the user name to see the number of friends: ")
                    friendship.number_of_friends(user)
                    display_num_friends = input("Do you want to see the number of friends for another user? (y/n) ")

            print(friendship.least_friends_str())
        print("Social Network:")
        for friend1 in self.network:
            friends = ', '.join(self.network[friend1])
            print(f"{friend1} -> {friends}")


class Friendship:
    def __init__(self, network):
        self.network = network
        self.friend_count = {}
        self.recommendations = {}


    def count_friends(self):
        for friend1 in self.network:
            self.friend_count[friend1] = 0
            for friend2 in self.network:
                if friend1 != friend2 and friend2 in self.network[friend1]:
                    self.friend_count[friend1] += 1

    def display_friend_count(self):
        self.count_friends()
        print("Common Friend Count:")
        for friend in self.friend_count:
            print(f"{friend}: {self.friend_count[friend]}")

    def recommend_friend(self, user):
        self.recommendations[user] = []
        if user in self.network:
            for friend in self.network[user]:
                for mutual_friend in self.network[friend]:
                    if (
                        mutual_friend != user
                        and mutual_friend not in self.network[user]
                        and mutual_friend not in self.recommendations[user]
                    ):
                        self.recommendations[user].append(mutual_friend)
            if self.recommendations[user]:
                print(f"Recommended friends for {user}: {', '.join(self.recommendations[user])}")
            else:
                print(f"No recommendations for {user}")
        else:
            print(f"User {user} not found in network")

    def number_of_friends(self, user):
        if user in self.network:
            print(f"{user} has {len(self.network[user])} friends.")
        else:
            print(f"User {user} not found in network")

    def least_friends_str(self):
        friend_count = Counter(len(friends) for friends in self.network.values())
        least_friends = [user for user, friends in self.network.items() if len(friends) == min(friend_count.keys())]
        zero_friends = [user for user, friends in self.network.items() if not friends]
        return f"Users with least friends: {least_friends}\nMembers with zero friends: {zero_friends}"


if __name__ == "__main__":
    # code to load social network
    sn = SocialNetwork()

    # code to loop through file names until user enters 'n'
    while True:
        file_name = input("Enter file name or type n to exit: ")
        if file_name == "n":
            break
        success = sn.load_network(file_name)
        if success:
            display_network = input("Do you want to display the network? (y/n) ")
            if display_network == "y":
                sn.display_network()
            friendship = Friendship(sn.network)  # Assign newly created instance to the same "friendship" variable
            display_friend_count = input("Do you want to display the common friend count? (y/n) ")
            if display_friend_count == "y":
                friendship.display_friend_count()  # Call display_friend_count method of the instance assigned to "friendship"

                recommend_friend = "y"
                while recommend_friend == "y":
                    user = input("Enter the user name to recommend friends: ")
                    friendship.recommend_friend(user)
                    recommend_friend = input("Do you want to recommend friends for another user? (y/n) ")

                display_num_friends = "y"
                while display_num_friends == "y":
                    user = input("Enter the user name to see number of friends: ")
                    friendship.number_of_friends(user)
                    display_num_friends = input("Do you want to see the number of friends for another user? (y/n) ")

            print(friendship.least_friends_str())
            # print(friendship.zero_friends_str())
        # else:
        #     print("File not found. Please enter a valid file name.")














from collections import Counter

# Define the SocialNetwork class
class SocialNetwork:
    def __init__(self):
        self.network = {}

    def load_network(self, file_name):
        try:
            with open(file_name, 'r') as file:
                num_members = int(file.readline().strip())
                for i in range(num_members):
                    line = file.readline().strip().split()
                    friend1, friend2 = line[0], line[1]
                    if friend1 not in self.network:
                        self.network[friend1] = []
                    if friend2 not in self.network:
                        self.network[friend2] = []
                    self.network[friend1].append(friend2)
                    self.network[friend2].append(friend1)
            print("File opened successfully")
            return True
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")
            return False

    def display_network(self):
        print("Social Network:")
        for friend1 in self.network:
            friends = ', '.join(self.network[friend1])
            print(f"{friend1} -> {friends}")

# Define the Friendship class
class Friendship:
    def __init__(self, network):
        self.network = network
        self.friend_count = {}
        self.recommendations = {}

    def count_friends(self):
        # Count common friends for each user
        self.friend_count = {user: sum(1 for friend in friends if friend != user) for user, friends in self.network.items()}

    def display_friend_count(self):
        self.count_friends()
        print("Common Friend Count:")
        for friend, count in self.friend_count.items():
            print(f"{friend}: {count}")

    # ... (rest of the methods)

if __name__ == "__main__":
    sn = SocialNetwork()
    friendship = Friendship(sn.network)

    while True:
        file_name = input("Enter file name or type 'n' to exit: ")
        if file_name == "n":
            break
        success = sn.load_network(file_name)
        if success:
            display_network = input("Do you want to display the network? (y/n) ")
            if display_network == "y":
                sn.display_network()

            display_friend_count = input("Do you want to display the common friend count? (y/n) ")
            if display_friend_count == "y":
                friendship.display_friend_count()

                recommend_friend = "y"
                while recommend_friend == "y":
                    user = input("Enter the user name to recommend friends: ")
                    friendship.recommend_friend(user)
                    recommend_friend = input("Do you want to recommend friends for another user? (y/n) ")

                display_num_friends = "y"
                while display_num_friends == "y":
                    user = input("Enter the user name to see the number of friends: ")
                    friendship.number_of_friends(user)
                    display_num_friends = input("Do you want to see the number of friends for another user? (y/n) ")

            print(friendship.least_friends_str())
