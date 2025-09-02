import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Maintxt extends StatelessWidget {
  final String txt;
  const Maintxt({super.key,required this.txt});

  @override
  Widget build(BuildContext context) {
    return  Align(
      alignment: Alignment.topLeft,
      child: Text(
        txt,
        style: TextStyle(
          color: Colors.black,
          fontSize: 23,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }
}
