import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Authtxtoftextfield extends StatelessWidget {
  final String txt;
  const Authtxtoftextfield({super.key,required this.txt});

  @override
  Widget build(BuildContext context) {
    return  Align(
      alignment: Alignment.topLeft,
      child: Text(
        txt,
        style: TextStyle(
          color: Colors.black,
          fontWeight: FontWeight.bold,
          fontSize: 17
        ),
      ),
    );
  }
}
