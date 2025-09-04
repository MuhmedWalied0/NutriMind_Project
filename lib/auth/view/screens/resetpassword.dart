import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/screens/successfullyScreen.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';

import '../widgets/txtfield.dart';

class Resetpassword extends StatelessWidget {
  const Resetpassword({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Padding(padding:  const EdgeInsets.symmetric(horizontal: 16),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
             const SizedBox(height: 230,),
            const Text(
              'Reset yout password',
              style: TextStyle(
                color: Colors.black,
                fontSize: 23,
                fontWeight: FontWeight.bold,
              ),),
             const SizedBox(height: 24,),
            const Text(
              'Enter Your New password',
              style: TextStyle(
                color: Color(0xff8A8A8A),
                fontSize: 14,
              ),
            ),
            const SizedBox(height: 50,),
            const CustomTextField(labelText: 'New Password', icona: Icons.password,),
            const SizedBox(height: 25,),
            const CustomTextField(labelText: 'Confirm Password', icona: Icons.password,),
            const SizedBox(height: 60,),
            Mainbutton(func: (){
              Navigator.push(context, MaterialPageRoute(builder: (context)=>Successfullyscreen()));
            }, txt: 'Update'),

          ],
        ),
        ),
      ),
    );
  }
}
