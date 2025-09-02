import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Mainbutton extends StatelessWidget {
  final VoidCallback func;
  final String txt;
  const Mainbutton({super.key,required this.func,required this.txt});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16.0),
      child: SizedBox(
        width: MediaQuery.of(context).size.width,
        height: 50,
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Color(0xff207344)
          ),
            onPressed:func,
            child: Text(txt,
            style: TextStyle(
              color:Colors.white,
              fontWeight: FontWeight.bold,
            ),
            )
        ),
      ),
    );
  }
}
