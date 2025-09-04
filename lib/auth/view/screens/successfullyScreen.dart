import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';

class Successfullyscreen extends StatelessWidget {
  const Successfullyscreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Padding(padding:  const EdgeInsets.symmetric(horizontal: 16),
        child:Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const SizedBox(height: 200,),
            Image.asset('assets/Sticker.png'),
            const Text(
              ' password Changed',
              style: TextStyle(
                color: Colors.black,
                fontSize: 23,
                fontWeight: FontWeight.bold,
              ),),
            const SizedBox(height: 34,),
            const Text(
              'the password successfully changed',
              style: TextStyle(
                color: Color(0xff8A8A8A),
                fontSize: 14,
              ),
            ),
            SizedBox(
              height: 80,
            ),
            Mainbutton(func: (){}, txt: 'Back to Sign In'),
          ],
        ) ,
        ),
      ),
    );
  }
}
