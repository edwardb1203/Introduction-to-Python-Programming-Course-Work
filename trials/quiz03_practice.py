"""Practice for quiz 03."""
from __future__ import annotations
__author__ = "730312903"


followers_list: List[str] = ["chris", "edd", "aiden", "poop"]
following_list: List[str] = ["uzi", "dt", "poop"]

def main() -> None:
    """Entry into our program."""
    Account1 = InstaUser("edward", "yallah")
    Account2 = InstaUser("aiden", "ok")
    Account3 = InstaUser("ford", "poo")
    Account4 = InstaUser("chris", "ko")
    Account1.addFollower(Account2)
    Account1.addFollower(Account3)
    Account1.addFollower(Account4)
    Account1.follow(Account3)
    Account1.following.append("aiden")
    print(Account1.getFollowerCount())
    print(Account1.getMutuals())
    print(Account1.followers)
    print(Account1.following)


class InstaUser:
    username: str
    password: str
    followers: List[str]
    following: List[str]

    def __init__(self, username: str, password: str):
        """Constructor for InstaUser class."""
        self.username = username
        self.password = password
        self.followers = []
        self.following = []

    def getFollowerCount(self) -> int:
        """Gets the follower count of an account."""
        return len(self.followers)
    
    def getFollowuingCount(self) -> int:
        """Gets the follwing count of an account."""
        return len(self.following)
    
    def getMutuals(self) -> List[str]:
        mutuals: List[str] = []
        for i in range(len(self.followers)):
            for j in range(len(self.following)):
                if self.followers[i] == self.following[j]:
                    mutuals.append(self.followers[i])
        return mutuals
    
    # def addFollower(self, name: str, password: str) -> None:
    #     person = InstaUser(name, password)
    #     self.followers.append(person.username)
    
    def addFollower(self, person: InstaUser) -> None:
        self.followers.append(person.username)
    
    def follow(self, person: InstaUser) -> None:
        self.following.append(person.username)
        person.addFollower(self)


if __name__ == "__main__":
    main()