package com.nankaijinnan.yolov8tflite;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.core.splashscreen.SplashScreen;
public class MainActivity2 extends AppCompatActivity {
    Button btnCameraLive,btnCapture;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        try {
            Thread.sleep(3000);
            SplashScreen.installSplashScreen(this);

        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        //installSplashScreen()
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main2);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        btnCameraLive=findViewById(R.id.button);
        btnCapture=findViewById(R.id.button2);
        btnCapture.setVisibility(View.INVISIBLE);

        btnCameraLive.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent myIntent = new Intent(MainActivity2.this, MainActivity.class);
                //myIntent.putExtra("key", value); //Optional parameters
                MainActivity2.this.startActivity(myIntent);
            }
        });

        btnCapture.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent myIntent = new Intent(MainActivity2.this, MainActivityLoad.class);
                //myIntent.putExtra("key", value); //Optional parameters
                MainActivity2.this.startActivity(myIntent);
            }
        });


    }
}