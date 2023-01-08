class Post {
  String body;
  String author;
  int likes = 0;
  bool userLikes = false;

  Post(this.body, this.author);

  void likesPost() {
    this.userLikes = !this.userLikes;
    if (this.userLikes) {
      this.likes += 1;
    } else {
      this.likes -= 1;
    }
  }
}
