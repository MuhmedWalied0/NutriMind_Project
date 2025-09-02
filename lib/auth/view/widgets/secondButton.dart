import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '../screens/signUp.dart';

class Secondbutton extends StatelessWidget {
  const Secondbutton({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16.0),
      child: SizedBox(
        width: MediaQuery.of(context).size.width,
        height: 50,
        child: ElevatedButton(
            style: ElevatedButton.styleFrom(
                backgroundColor: Colors.white,
              side: BorderSide(
                color:Color(0xff207344)
              )
            ),
            onPressed: (){
              Navigator.push(context, MaterialPageRoute(builder: (context)=>Signup()));
            },
            child: Text('Sign Up',
              style: TextStyle(
                color:Color(0xff207344),
                fontWeight: FontWeight.bold,
              ),
            ),
        ),
      ),
    );
  }
}
