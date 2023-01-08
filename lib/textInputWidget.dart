import 'package:flutter/material.dart';

// ignore: must_be_immutable
class TextInputWidget extends StatefulWidget {
  final Function(String) callback;
  // ignore: prefer_const_constructors_in_immutables
  TextInputWidget(this.callback, {super.key});

  @override
  // ignore: library_private_types_in_public_api
  _TextInputWidgetState createState() => _TextInputWidgetState();
}

class _TextInputWidgetState extends State<TextInputWidget> {
  final controller = TextEditingController();

  @override
  void dispose() {
    super.dispose();
    controller.dispose();
  }

  void click() {
    widget.callback(controller.text);
    FocusScope.of(context).unfocus();
    controller.clear();
  }

  @override
  Widget build(BuildContext context) {
    return TextField(
        controller: controller,
        decoration: InputDecoration(
            prefixIcon: const Icon(Icons.message),
            labelText: "Type a message:",
            suffixIcon: IconButton(
              icon: const Icon(Icons.send),
              splashColor: Colors.blue,
              tooltip: "Post message",
              onPressed: this.click,
            )));
  }
}
