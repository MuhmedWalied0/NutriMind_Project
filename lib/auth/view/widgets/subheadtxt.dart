import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Subheadtxt extends StatelessWidget {
  final String txt;
  const Subheadtxt({super.key,required this.txt});

  @override
  Widget build(BuildContext context) {
    return  Align(
      alignment: Alignment.topLeft,
      child: Text(
        txt,
        style: TextStyle(
            color: Color(0xff8A8A8A),
            fontSize: 14,
        ),
      ),
    );
  }
}
