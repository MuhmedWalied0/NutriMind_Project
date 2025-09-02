import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class DontHaveAccount extends StatelessWidget {
  final String normaltext;
  final String buttontext;
  final VoidCallback func;
  const DontHaveAccount({super.key,
  required this.buttontext,
    required this.normaltext,
    required this.func
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
        children: [
           Text(normaltext,
          style:const  TextStyle(
            color:Colors.black,
          ),
          ),
          TextButton(onPressed: func,
              child:  Text(buttontext,
              style:const TextStyle(
                color: Color(0xff207344),
              ),
              ))
        ],
    );
  }
}
