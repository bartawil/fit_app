// ignore_for_file: unnecessary_this

import 'package:fit_app/login.dart';
import 'package:flutter/material.dart';
import 'myHomePage.dart';
import 'login.dart';

void main() {
  //check jira
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  // This widget is the root of your application
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'tims App',
      theme: ThemeData(
        primarySwatch: Colors.lightGreen,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const LoginPage(),
    );
  }
}
