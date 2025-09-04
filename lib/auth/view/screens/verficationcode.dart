import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pin_code_fields/pin_code_fields.dart';
import 'package:tester/auth/view/screens/resetpassword.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';

import '../widgets/secondButton.dart';

class Verficationcode extends StatelessWidget {
  const Verficationcode({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Padding(padding: const EdgeInsets.symmetric(horizontal: 16),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const SizedBox(height: 230,),
          Text(
            'Check your phone',
            style: TextStyle(
              color: Colors.black,
              fontSize: 23,
              fontWeight: FontWeight.bold,
            ),),
            const SizedBox(height: 24,),
            Text(
              'We have send code to your email',
              style: TextStyle(
                color: Color(0xff8A8A8A),
                fontSize: 14,
              ),
            ),
            const SizedBox(height: 30,),
            PinCodeTextField(
              appContext: context,
              length: 4,
              keyboardType: TextInputType.number,
              obscureText: false,
              animationType: AnimationType.fade,
              pinTheme: PinTheme(
                shape: PinCodeFieldShape.box,
                borderRadius: BorderRadius.circular(12),
                fieldHeight: 80,
                fieldWidth: 60,
                activeFillColor: Colors.white,
                inactiveFillColor: Colors.grey[200],
                selectedFillColor: Colors.white,
                activeColor: Colors.green,
                selectedColor: Colors.blue,
                inactiveColor: Colors.grey,
              ),
              animationDuration: const Duration(milliseconds: 300),
              backgroundColor: Colors.transparent,
              enableActiveFill: true,
              onChanged: (value) {},
            ),

            const Text('Code expire in 24 hour',
            style: TextStyle(
              color: Colors.black,
              fontSize: 14
            ),
            ),
            const SizedBox(height: 40,),
            Mainbutton(func: (){
              Navigator.push(context, MaterialPageRoute(builder: (context)=>Resetpassword()));
            }, txt: 'Verify'),
            SizedBox(height: 24,),
            Secondbutton(txt: 'Send Again',),

          ],
        ),
        ),
      ),
    );
  }
}




