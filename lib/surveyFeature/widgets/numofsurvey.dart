import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class NumOfSurvey extends StatelessWidget {
  final String num;
  const NumOfSurvey({
    required this.num,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return  Align(
      alignment: Alignment.topRight,
      child:  Text(num,
        style:const  TextStyle(
            color: Colors.green,
            fontWeight: FontWeight.bold,
            fontSize: 20
        ),
      ),
    );
  }
}