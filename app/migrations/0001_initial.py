# Generated by Django 3.1.7 on 2022-05-17 13:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Application name', max_length=250)),
                ('description', models.TextField(blank=True, help_text='Brief application description')),
                ('url', models.URLField()),
                ('icon', models.ImageField(upload_to='icons/')),
                ('active', models.BooleanField(default=True, help_text='Is this application active?')),
                ('shown', models.BooleanField(default=False, help_text='Is this application visible?')),
                ('code_repo_url', models.URLField(blank=True, help_text='Code repository location', max_length=250)),
                ('design_documentation_url', models.URLField(blank=True, help_text='Design documentation location', max_length=250)),
                ('platform_description', models.TextField(blank=True, help_text='Brief description of platform used in the app')),
                ('deployment_env_further_details', models.TextField(blank=True, help_text='Further details about the deployment environment')),
                ('date_released', models.DateField(default=django.utils.timezone.now, help_text='Approximate date the application was released')),
                ('date_decommissioned', models.DateField(blank=True, help_text='Approximate date the application was decommissioned', null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the dataset', max_length=250)),
                ('description', models.TextField(blank=True, help_text='Brief description of the dataset')),
                ('url', models.URLField(blank=True, help_text='Dataset location')),
                ('credentials', models.TextField(blank=True, help_text='Credentials for accessing the dataset')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeploymentEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the deployment environment', max_length=250)),
                ('description', models.TextField(blank=True, help_text='Brief description of the deployment environment')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the organization', max_length=250)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('icon', models.ImageField(upload_to='icons/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Service Name', max_length=250)),
                ('description', models.TextField()),
                ('service_catalog_url', models.URLField(help_text='Reference to the SERVIR Service catalog')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the service area', max_length=250)),
                ('description', models.TextField()),
                ('service_catalog_url', models.URLField(blank=True, help_text='Reference to the SEVIR Service catalog')),
                ('icon', models.ImageField(upload_to='icons/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_entry', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.application')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the developer', max_length=250)),
                ('photo', models.ImageField(upload_to='icons/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True, help_text='Is the developer active?')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organization')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='datasets',
            field=models.ManyToManyField(blank=True, to='app.Dataset'),
        ),
        migrations.AddField(
            model_name='application',
            name='deployment_environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.deploymentenvironment'),
        ),
        migrations.AddField(
            model_name='application',
            name='organization',
            field=models.ForeignKey(help_text='Organization that developed the application', on_delete=django.db.models.deletion.CASCADE, to='app.organization'),
        ),
        migrations.AddField(
            model_name='application',
            name='primary_developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.developer'),
        ),
        migrations.AddField(
            model_name='application',
            name='serviceareas',
            field=models.ManyToManyField(blank=True, to='app.ServiceArea'),
        ),
    ]
