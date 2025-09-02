import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/screens/signinScreen.dart';

import '../widgets/mainButton.dart';
import '../widgets/secondButton.dart';

class Welcomeaurth extends StatelessWidget {
  const Welcomeaurth({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Image.asset('assets/auth.png'),
          SizedBox(height: 160,),
          Mainbutton(func: () {Navigator.push(context, MaterialPageRoute(builder: (context)=>Signinscreen())
          );
          }, txt: 'Sign In',
          ),
          SizedBox(height: 16,),
          Secondbutton(),
        ],
      ),
    );
  }
}
